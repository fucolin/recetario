"""Contrato recetario-1.1. Validación y proyección de metadatos para lectores previos.

La proyección es un adaptador de preparación, no activa un menú ni resuelve elecciones.
"""
import copy, re

ID = re.compile(r'cm-ing-\d{6}')

def require(ok, message):
    if not ok: raise ValueError(message)

def index_registry(registry):
    products=registry.get('products',[])
    require(registry.get('schemaVersion')==1 and bool(products),'Registro inválido')
    result={}
    for p in products:
        require(isinstance(p.get('id'),str) and ID.fullmatch(p['id']) and p['id'] not in result,'ID inválido o duplicado')
        require(isinstance(p.get('nombre'),str) and p['nombre'].strip()==p['nombre'] and bool(p['nombre']),'Nombre inválido')
        result[p['id']]=p
    require(type(registry.get('nextNumber')) is int and registry['nextNumber']>max(int(i[-6:]) for i in result),'Secuencia inválida')
    return result

def validate(recipe, registry):
    idx=index_registry(registry)
    require(recipe.get('esquema')=='recetario-1.1','Versión desconocida')
    def reference(value):require(isinstance(value,str) and value in idx,'Referencia inexistente')
    def line(i, nested=False):
        require(isinstance(i,dict) and isinstance(i.get('nombre'),str) and bool(i['nombre'].strip()),'Ingrediente inválido')
        if 'catalogo_ref' in i:reference(i['catalogo_ref'])
        options=i.get('alternativas')
        if options is not None:
            require(not nested and i.get('seleccion')=='una' and isinstance(options,list) and len(options)>=2,'Alternativa inválida')
            refs=[]
            for option in options:
                line(option,True);require('catalogo_ref' in option,'Rama sin referencia');refs.append(option['catalogo_ref'])
            require(len(refs)==len(set(refs)),'Ramas duplicadas')
        else: require('catalogo_ref' in i,'Ingrediente sin referencia')
        if i.get('es_condimento') is False:require('tipo_condimento' not in i,'Tipo con condimento falso')
        if i.get('es_condimento') is True:require(i.get('tipo_condimento') in {'sal_y_especias','hierbas_aromaticas','aromaticos_frescos','aceites_acidos_y_salsas','fondos_para_cocinar'},'Tipo de condimento inválido')
    require(isinstance(recipe.get('ingredientes'),list) and bool(recipe['ingredientes']),'Sin ingredientes')
    for i in recipe['ingredientes']:line(i)
    basics=recipe.get('ingredientes_basicos')
    def basic_reference(value):
        if isinstance(value, str):
            reference(value)
            return
        require(isinstance(value, dict) and set(value) == {'nombre', 'una_de'},
                'Elección de básico inválida')
        choices = value['una_de']
        require(isinstance(choices, list) and len(choices) >= 2, 'Elección incompleta')
        for ref in choices:
            reference(ref)
        require(len(set(choices)) == len(choices), 'Elección duplicada')
        require(any(line.get('nombre') == value['nombre'] and
                    line.get('seleccion') == 'una' and
                    [option['catalogo_ref'] for option in line['alternativas']] == choices
                    for line in recipe['ingredientes']), 'Elección sin línea correspondiente')

    require(isinstance(basics,list) and bool(basics),'Básicos inválidos')
    for n, ref in enumerate(basics):
        basic_reference(ref)
        require(ref not in basics[:n], 'Básico duplicado')
    for o in recipe.get('ingredientes_basicos_opciones',[]):
        require(o.get('tipo') in {'alternativa','opcional'} and isinstance(o.get('ingredientes'),list) and bool(o['ingredientes']),'Opción básica inválida')
        for ref in o['ingredientes']:reference(ref)
        for ref in o.get('sustituye',[]):basic_reference(ref);require(ref in basics,'Sustitución sin básico')
    for o in recipe.get('condimentos_opciones',[]):
        reference(o.get('catalogo_ref'))
        parts=re.findall(r'([a-z_]+)|\[(\d+)\]',o.get('origen',''))
        require(bool(parts),'Origen vacío')
        value=recipe
        try:
            for key,n in parts:value=value[key] if key else value[int(n)]
        except (IndexError,KeyError,TypeError):raise ValueError('Origen inexistente')
        require(isinstance(value,str),'Origen no textual')
    return recipe

def metadata_for_legacy_reader(recipe, registry):
    """Proyecta IDs a nombres para motores previos; nunca escoge una alternativa.

    Conservar original y versión junto a la proyección. Antes de integrar, enlazar
    al transporte y a la hidratación reales y contrastar sus pruebas.
    """
    validate(recipe,registry)
    idx=index_registry(registry)
    names={ref:p['nombre'] for ref,p in idx.items()}
    for i in recipe['ingredientes']:
        if 'catalogo_ref' in i:names[i['catalogo_ref']]=i['nombre']
        for branch in i.get('alternativas',[]):names[branch['catalogo_ref']]=branch['nombre']
    result={k:copy.deepcopy(recipe[k]) for k in ['ingredientes_basicos','ingredientes_basicos_opciones','condimentos_opciones'] if k in recipe}
    def basic_name(ref):
        return ref['nombre'] if isinstance(ref, dict) else names[ref]
    result['ingredientes_basicos']=[basic_name(ref) for ref in result['ingredientes_basicos']]
    for o in result.get('ingredientes_basicos_opciones',[]):
        o['ingredientes']=[names[ref] for ref in o['ingredientes']]
        if 'sustituye' in o:o['sustituye']=[basic_name(ref) for ref in o['sustituye']]
    return result

def select_alternative(line, selected_id=None):
    """Devuelve cero o una rama. No hereda cantidades ni producto preferido.

    La cantidad común del grupo describe una elección, no cada rama simultánea.
    La decisión de incluir un uso básico no elegido corresponde al motor/menú.
    """
    require(line.get('seleccion')=='una','No es una alternativa')
    if selected_id is None:return []
    branches=[b for b in line['alternativas'] if b['catalogo_ref']==selected_id]
    require(len(branches)==1,'Elección ajena al grupo')
    return copy.deepcopy(branches)

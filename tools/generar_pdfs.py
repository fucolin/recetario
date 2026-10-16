#!/usr/bin/env python3
"""Genera los PDF A4 del recetario con una única plantilla visual."""

from __future__ import annotations

import argparse
from datetime import date
import json
import math
import re
from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas


# Contrato visual del recetario. No duplicar estos valores en otros scripts.
VERDE_OSCURO = "#286348"
VERDE_TEXTO = "#314039"
VERDE_SECUNDARIO = "#61766B"
FONDO_INGREDIENTES = "#F3F6F1"
LINEA_PIE = "#C8D7CC"

TIPOS_FICHA = {
    "receta": "Receta",
    "preparacion": "Preparación sencilla",
    "combinacion": "Combinación",
}

MARGEN_X = 49
ANCHO_CONTENIDO = A4[0] - 2 * MARGEN_X
PIE_Y = 28


def normalizar(texto: str) -> str:
    return texto.replace("–", "-").replace("‑", "-")


def partir_lineas(texto: str, fuente: str, tamano: float, ancho: float) -> list[str]:
    palabras = normalizar(texto).split()
    lineas: list[str] = []
    actual = ""
    for palabra in palabras:
        candidato = f"{actual} {palabra}".strip()
        if actual and stringWidth(candidato, fuente, tamano) > ancho:
            lineas.append(actual)
            actual = palabra
        else:
            actual = candidato
    if actual:
        lineas.append(actual)
    return lineas


def dibujar_texto_envuelto(c, texto, x, y, ancho, fuente, tamano, interlineado, color):
    c.setFont(fuente, tamano)
    c.setFillColor(HexColor(color))
    for linea in partir_lineas(texto, fuente, tamano, ancho):
        c.drawString(x, y, linea)
        for enlace in getattr(c, "enlaces_texto", []):
            texto_enlace = normalizar(enlace["texto"])
            inicio = linea.find(texto_enlace)
            if inicio >= 0:
                x1 = x + stringWidth(linea[:inicio], fuente, tamano)
                x2 = x1 + stringWidth(texto_enlace, fuente, tamano)
                c.linkURL(enlace["url"], (x1, y - 2, x2, y + tamano), relative=0)
                c.setStrokeColor(HexColor(VERDE_OSCURO))
                c.setLineWidth(0.4)
                c.line(x1, y - 1, x2, y - 1)
        y -= interlineado
    return y


def ingredientes_para_pdf(receta: dict) -> list[str]:
    if receta.get("pdf_ingredientes"):
        return [normalizar(item) for item in receta["pdf_ingredientes"]]
    raise ValueError(
        f"{receta.get('id', 'receta')}: falta 'pdf_ingredientes'; "
        "se exige una lista editorial explícita para no alterar cantidades"
    )


def dibujar_ingredientes(c, ingredientes: list[str], y_superior: float) -> float:
    """Dibuja la caja canónica: sin viñetas, dos columnas y #F3F6F1."""
    filas = math.ceil(len(ingredientes) / 2)
    alto = max(96, 22 * filas + 18)
    y_inferior = y_superior - alto
    c.setFillColor(HexColor(FONDO_INGREDIENTES))
    c.rect(MARGEN_X, y_inferior, ANCHO_CONTENIDO, alto, stroke=0, fill=1)

    columna_1 = ingredientes[:filas]
    columna_2 = ingredientes[filas:]
    x_columnas = (MARGEN_X + 10, MARGEN_X + ANCHO_CONTENIDO / 2 + 7)
    ancho_columna = ANCHO_CONTENIDO / 2 - 19
    tamano = 8.4
    interlineado = 10.1
    paso_fila = (alto - 18) / filas
    for columna, x in zip((columna_1, columna_2), x_columnas):
        for fila, ingrediente in enumerate(columna):
            y = y_superior - 15 - fila * paso_fila
            dibujar_texto_envuelto(
                c, ingrediente, x, y, ancho_columna,
                "Helvetica", tamano, interlineado, VERDE_TEXTO,
            )
    return y_inferior


def generar_pdf(receta: dict, destino: Path) -> None:
    fecha_actualizacion = date.fromisoformat(receta["fecha_actualizacion"]).strftime("%d/%m/%Y")
    ingredientes = ingredientes_para_pdf(receta)
    if any(re.match(r"^\s*[•◦*-]\s+", item) for item in ingredientes):
        raise ValueError("Los ingredientes del PDF no pueden contener viñetas")

    tipo = receta.get("tipo_ficha", "receta")
    if tipo not in TIPOS_FICHA:
        raise ValueError(f"{receta['id']}: tipo_ficha no reconocido: {tipo}")
    if tipo != "receta":
        raise ValueError(f"{receta['id']}: solo las fichas de tipo receta generan PDF")
    pasos = receta.get("pasos") or []
    if not pasos:
        raise ValueError(f"{receta['id']}: una receta necesita pasos")

    destino.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(destino), pagesize=A4, pageCompression=1)
    c.enlaces_texto = receta.get("enlaces_texto", [])
    ancho, alto = A4

    titulo = normalizar(receta["titulo"]).upper()
    tamano_titulo = 18 if len(titulo) < 42 else 15.6
    y = alto - 52
    y = dibujar_texto_envuelto(
        c, titulo, MARGEN_X, y, ANCHO_CONTENIDO,
        "Helvetica-Bold", tamano_titulo, tamano_titulo * 1.15, VERDE_TEXTO,
    )

    raciones = receta["raciones"]
    tiempo = receta["tiempo_total_min"]
    texto_raciones = (
        str(raciones["min"])
        if raciones["min"] == raciones["max"]
        else f"{raciones['min']}-{raciones['max']}"
    )
    etiqueta_raciones = "ración" if raciones["min"] == raciones["max"] == 1 else "raciones"
    meta = (
        f"{receta['subtitulo']} · {texto_raciones} {etiqueta_raciones} "
        f"· {tiempo['min']}-{tiempo['max']} min · {TIPOS_FICHA[tipo]}"
    )
    if receta.get("variante") and receta["variante"] != "principal":
        meta += f" · Versión {receta['variante'].replace('g', ' g')}"
    y -= 3
    y = dibujar_texto_envuelto(
        c, meta, MARGEN_X, y, ANCHO_CONTENIDO,
        "Helvetica", 9.5, 11.5, VERDE_SECUNDARIO,
    )

    y -= 21
    c.setFont("Helvetica-Bold", 11.3)
    c.setFillColor(HexColor(VERDE_OSCURO))
    c.drawString(MARGEN_X, y, "INGREDIENTES")
    y = dibujar_ingredientes(c, ingredientes, y - 10) - 24

    if pasos:
        c.setFont("Helvetica-Bold", 11.3)
        c.setFillColor(HexColor(VERDE_OSCURO))
        c.drawString(MARGEN_X, y, "PREPARACIÓN")
        y -= 20

        densidad = sum(len(p["instrucciones"]) for p in pasos)
        tamano_pasos = 8.15 if densidad > 900 else 8.45
        interlineado = tamano_pasos * 1.35
        separacion = 5.8 if densidad > 900 else 7.2
        for paso in pasos:
            encabezado = f"{paso['orden']}. {paso['titulo']} · {paso['duracion_texto']}"
            y = dibujar_texto_envuelto(
                c, encabezado, MARGEN_X, y, ANCHO_CONTENIDO,
                "Helvetica-Bold", tamano_pasos + 0.2, interlineado, VERDE_OSCURO,
            )
            y = dibujar_texto_envuelto(
                c, paso["instrucciones"], MARGEN_X, y, ANCHO_CONTENIDO,
                "Helvetica", tamano_pasos, interlineado, VERDE_TEXTO,
            )
            y -= separacion
    claves = receta.get("claves")
    if claves:
        y = dibujar_texto_envuelto(
            c, f"CLAVES: {claves}", MARGEN_X, y - 1, ANCHO_CONTENIDO,
            "Helvetica", 8.05, 10.4, VERDE_TEXTO,
        )
    if y < PIE_Y + 26:
        raise ValueError(f"{receta['id']}: el contenido invade el pie de página")

    c.setStrokeColor(HexColor(LINEA_PIE))
    c.setLineWidth(0.45)
    c.line(MARGEN_X, PIE_Y + 11, ancho - MARGEN_X, PIE_Y + 11)
    c.setFont("Helvetica", 7.4)
    c.setFillColor(HexColor(VERDE_SECUNDARIO))
    c.drawString(MARGEN_X, PIE_Y, f"Fecha: {fecha_actualizacion}")
    c.save()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("recetas", nargs="*", help="JSON concretos; por defecto, todas las recetas")
    parser.add_argument("--salida", default="build/pdfs", help="Directorio de salida")
    args = parser.parse_args()

    raiz = Path(__file__).resolve().parent.parent
    fuentes = [Path(p) for p in args.recetas] or sorted(
        p for p in raiz.glob("*.json") if not p.name.endswith(".schema.json")
    )
    salida = Path(args.salida)
    if not salida.is_absolute():
        salida = raiz / salida

    for fuente in fuentes:
        if not fuente.is_absolute():
            fuente = Path.cwd() / fuente
        receta = json.loads(fuente.read_text(encoding="utf-8"))
        if receta.get("tipo_ficha", "receta") != "receta":
            print(f"Omitido {receta['id']}: no necesita PDF")
            continue
        destino = salida / f"{receta['id']}.pdf"
        generar_pdf(receta, destino)
        print(destino)


if __name__ == "__main__":
    main()

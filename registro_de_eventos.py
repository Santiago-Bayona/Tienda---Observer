"""3.3 Suscriptor concreto: guarda cada evento en una lista (y opcionalmente en archivo)."""
from __future__ import annotations

from datetime import datetime
from typing import Any

from suscriptor import Suscriptor


class RegistroDeEventos(Suscriptor):
    def __init__(self, ruta_archivo: str | None = None) -> None:
        self.registros: list[str] = []
        self.ruta_archivo = ruta_archivo

    def actualizar(self, datos: dict[str, Any]) -> None:
        linea = f"{datetime.now():%Y-%m-%d %H:%M:%S} | {datos['evento']} | {datos['producto']}"
        self.registros.append(linea)
        if self.ruta_archivo:
            with open(self.ruta_archivo, "a", encoding="utf-8") as f:
                f.write(linea + "\n")

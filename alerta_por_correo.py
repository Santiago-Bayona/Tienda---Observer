"""3.3 Suscriptor concreto: simula el envío de un correo con print."""
from __future__ import annotations

from typing import Any

from suscriptor import Suscriptor


class AlertaPorCorreo(Suscriptor):
    def __init__(self, correo: str) -> None:
        self.correo = correo
        self.enviados: list[str] = []

    def actualizar(self, datos: dict[str, Any]) -> None:
        asunto = f"Alerta {datos['evento']}: {datos['producto']}"
        self.enviados.append(asunto)
        print(f"[correo -> {self.correo}] Asunto: {asunto}")

"""4.2 Cuarto suscriptor: se agrega sin modificar Tienda ni GestorEventos."""
from __future__ import annotations

from typing import Any

from suscriptor import Suscriptor


class NotificacionPush(Suscriptor):
    def __init__(self, canal: str) -> None:
        self.canal = canal
        self.enviadas: list[str] = []

    def actualizar(self, datos: dict[str, Any]) -> None:
        texto = f"{datos['producto']} disponible"
        self.enviadas.append(texto)
        print(f"[push:{self.canal}] {texto}")

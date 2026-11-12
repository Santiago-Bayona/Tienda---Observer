"""3.3 Suscriptor concreto: imprime un aviso con su nombre."""
from __future__ import annotations

from typing import Any

from suscriptor import Suscriptor
from tienda import PRODUCTO_DISPONIBLE


class ClienteInteresado(Suscriptor):
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.avisos: list[str] = []

    def actualizar(self, datos: dict[str, Any]) -> None:
        if datos["evento"] == PRODUCTO_DISPONIBLE:
            msg = f"[{self.nombre}] ¡{datos['producto']} ya está disponible en {datos['tienda']}!"
        else:
            anterior = datos["precio_anterior"] or "sin precio"
            msg = (f"[{self.nombre}] {datos['producto']} cambió de precio: "
                   f"{anterior} -> {datos['precio_nuevo']}")
        self.avisos.append(msg)
        print(msg)

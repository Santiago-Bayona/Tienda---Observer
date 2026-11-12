"""3.2 Notificador."""
from __future__ import annotations

from gestor_eventos import GestorEventos

PRODUCTO_DISPONIBLE = "producto_disponible"
PRECIO_CAMBIADO = "precio_cambiado"


class Tienda:

    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.eventos = GestorEventos(PRODUCTO_DISPONIBLE, PRECIO_CAMBIADO)
        self._disponibles: set[str] = set()
        self._precios: dict[str, float] = {}

    def reabastecer(self, producto: str) -> None:
        if producto not in self._disponibles:
            self._disponibles.add(producto)
            self.eventos.notificar(PRODUCTO_DISPONIBLE,
                                   {"tienda": self.nombre, "producto": producto})

    def agotar(self, producto: str) -> None:
        self._disponibles.discard(producto)

    def cambiar_precio(self, producto: str, precio: float) -> None:
        anterior = self._precios.get(producto)
        self._precios[producto] = precio
        self.eventos.notificar(PRECIO_CAMBIADO, {
            "tienda": self.nombre, "producto": producto,
            "precio_anterior": anterior, "precio_nuevo": precio,
        })

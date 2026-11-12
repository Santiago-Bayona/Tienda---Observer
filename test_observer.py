"""3.6 Pruebas del sistema de eventos."""
from __future__ import annotations

import unittest
from typing import Any

from alerta_por_correo import AlertaPorCorreo
from cliente_interesado import ClienteInteresado
from registro_de_eventos import RegistroDeEventos
from tienda import PRECIO_CAMBIADO, PRODUCTO_DISPONIBLE, Tienda


class TestObserverTienda(unittest.TestCase):
    def setUp(self) -> None:
        self.tienda = Tienda("Prueba")
        self.cliente = ClienteInteresado("Ana")

    def test_recibe_evento_suscrito(self) -> None:
        self.tienda.eventos.suscribir(PRODUCTO_DISPONIBLE, self.cliente)
        self.tienda.reabastecer("Teclado")
        self.assertEqual(len(self.cliente.avisos), 1)
        self.assertIn("Teclado", self.cliente.avisos[0])

    def test_no_recibe_eventos_de_otro_tipo(self) -> None:
        self.tienda.eventos.suscribir(PRODUCTO_DISPONIBLE, self.cliente)
        self.tienda.cambiar_precio("Teclado", 100_000)
        self.assertEqual(self.cliente.avisos, [])

    def test_tras_cancelar_no_recibe_mas(self) -> None:
        self.tienda.eventos.suscribir(PRODUCTO_DISPONIBLE, self.cliente)
        self.tienda.reabastecer("Teclado")
        self.tienda.eventos.cancelar(PRODUCTO_DISPONIBLE, self.cliente)
        self.tienda.reabastecer("Mouse")
        self.assertEqual(len(self.cliente.avisos), 1)

    def test_varios_suscriptores_todos_notificados(self) -> None:
        registro = RegistroDeEventos()
        correo = AlertaPorCorreo("a@b.com")
        for s in (self.cliente, registro, correo):
            self.tienda.eventos.suscribir(PRODUCTO_DISPONIBLE, s)
        self.tienda.reabastecer("Monitor")
        self.assertEqual(len(self.cliente.avisos), 1)
        self.assertEqual(len(registro.registros), 1)
        self.assertEqual(len(correo.enviados), 1)

    def test_suscriptor_funcional(self) -> None:
        recibidos: list[dict[str, Any]] = []
        self.tienda.eventos.suscribir(PRECIO_CAMBIADO, lambda d: recibidos.append(d))
        self.tienda.cambiar_precio("Monitor", 800_000)
        self.assertEqual(recibidos[0]["precio_nuevo"], 800_000)


if __name__ == "__main__":
    unittest.main(verbosity=2)

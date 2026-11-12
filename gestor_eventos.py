"""3.1 Gestor de eventos: guarda y notifica a los suscriptores."""
from __future__ import annotations

from typing import Any

from suscriptor import Oyente, Suscriptor


class GestorEventos:

    def __init__(self, *tipos_evento: str) -> None:
        self._suscriptores: dict[str, list[Oyente]] = {t: [] for t in tipos_evento}

    def suscribir(self, tipo_evento: str, suscriptor: Oyente) -> None:
        lista = self._suscriptores.setdefault(tipo_evento, [])
        if suscriptor not in lista:
            lista.append(suscriptor)

    def cancelar(self, tipo_evento: str, suscriptor: Oyente) -> None:
        lista = self._suscriptores.get(tipo_evento, [])
        if suscriptor in lista:
            lista.remove(suscriptor)

    def notificar(self, tipo_evento: str, datos: dict[str, Any]) -> None:
        datos = {"evento": tipo_evento, **datos}
        for suscriptor in list(self._suscriptores.get(tipo_evento, [])):
            if isinstance(suscriptor, Suscriptor):
                suscriptor.actualizar(datos)
            else:
                suscriptor(datos)

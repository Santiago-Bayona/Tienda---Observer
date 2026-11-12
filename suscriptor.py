from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Callable, Union


class Suscriptor(ABC):
    """Interfaz suscriptora: todo suscriptor concreto implementa actualizar()."""

    @abstractmethod
    def actualizar(self, datos: dict[str, Any]) -> None:
        pass


# Un suscriptor puede ser un objeto Suscriptor o una función (Actividad 3.7).
Oyente = Union[Suscriptor, Callable[[dict[str, Any]], None]]

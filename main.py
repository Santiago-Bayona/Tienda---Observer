"""3.4 y 3.5 Cliente: configura la tienda y sus suscriptores. 3.7 variante funcional."""
from __future__ import annotations

from typing import Any

from alerta_por_correo import AlertaPorCorreo
from cliente_interesado import ClienteInteresado
from notificacion_push import NotificacionPush
from registro_de_eventos import RegistroDeEventos
from tienda import PRECIO_CAMBIADO, PRODUCTO_DISPONIBLE, Tienda


# 3.7 Variante funcional: un suscriptor que es solo una función.
def aviso_sms(datos: dict[str, Any]) -> None:
    print(f"[SMS] {datos['producto']}: nuevo precio {datos['precio_nuevo']}")


def main() -> None:
    tienda = Tienda("TecnoUQ")

    ana = ClienteInteresado("Ana")
    luis = ClienteInteresado("Luis")
    registro = RegistroDeEventos()
    correo = AlertaPorCorreo("ventas@tecnouq.com")
    push = NotificacionPush("app-movil")

    # Ana solo quiere disponibilidad; Luis solo precios.
    tienda.eventos.suscribir(PRODUCTO_DISPONIBLE, ana)
    tienda.eventos.suscribir(PRECIO_CAMBIADO, luis)
    # El registro escucha todo; correo y push solo disponibilidad.
    tienda.eventos.suscribir(PRODUCTO_DISPONIBLE, registro)
    tienda.eventos.suscribir(PRECIO_CAMBIADO, registro)
    tienda.eventos.suscribir(PRODUCTO_DISPONIBLE, correo)
    tienda.eventos.suscribir(PRODUCTO_DISPONIBLE, push)
    # Suscriptor funcional (3.7)
    tienda.eventos.suscribir(PRECIO_CAMBIADO, aviso_sms)

    print("=== 1. Reabastecer teclado ===")
    tienda.reabastecer("Teclado mecánico")

    print("\n=== 2. Cambiar precio teclado ===")
    tienda.cambiar_precio("Teclado mecánico", 189_900)

    print("\n=== 3. Ana cancela su suscripción (3.5) ===")
    tienda.eventos.cancelar(PRODUCTO_DISPONIBLE, ana)
    tienda.reabastecer("Mouse inalámbrico")

    print(f"\nAvisos recibidos por Ana:  {len(ana.avisos)}")
    print(f"Avisos recibidos por Luis: {len(luis.avisos)}")
    print(f"Eventos en el registro:    {len(registro.registros)}")
    print(f"Correos enviados:          {len(correo.enviados)}")


if __name__ == "__main__":
    main()

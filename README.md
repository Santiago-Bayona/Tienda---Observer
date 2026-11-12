# Observer – Tienda con avisos de disponibilidad

Requisitos: Python 3.10+ (solo librería estándar).

## Ejecutar la demo
    python main.py

## Ejecutar las pruebas
    python -m unittest -v
    # o con pytest:  pytest -v

## Archivos (una clase por archivo)
| Archivo                  | Clase / contenido                    | Actividad |
|--------------------------|--------------------------------------|-----------|
| suscriptor.py            | `Suscriptor` (interfaz, abc.ABC)     | 3.1       |
| gestor_eventos.py        | `GestorEventos`                      | 3.1       |
| tienda.py                | `Tienda` (notificador)               | 3.2       |
| cliente_interesado.py    | `ClienteInteresado`                  | 3.3       |
| registro_de_eventos.py   | `RegistroDeEventos`                  | 3.3       |
| alerta_por_correo.py     | `AlertaPorCorreo`                    | 3.3       |
| notificacion_push.py     | `NotificacionPush` (cuarto suscriptor) | 4.2     |
| main.py                  | Cliente, baja en ejecución, `aviso_sms` | 3.4, 3.5, 3.7 |
| test_observer.py         | Pruebas (unittest)                   | 3.6       |

Para agregar un suscriptor nuevo basta con crear un archivo con una clase que
herede de `Suscriptor` (o una función con firma `(datos)`) y suscribirla en
`main.py`. `Tienda` no se modifica.

from datetime import date
from src.modelo.Trabajador import Trabajador
from src.modelo.Bonificacion import Bonificacion
from src.modelo.Descuento import Descuento
from src.modelo.declarative_base import Base, engine, Session

# create a new session
session = Session()
# 3 - extract all movies
trabajadores = session.query(Trabajador).all()

# Imprimir trabajadores
print('\n### Todos los trabajadores:')
for trabajador in trabajadores:
    print(f'Id: {trabajador.id} - Mes-Año: {trabajador.mesAnio} - Nombre: {trabajador.nombreTrabajador:25} - Sueldo básico: {trabajador.sueldoBasico}')
print('')

print("Join 1: Trabajador, Descuento")
result = session.query(Trabajador).join(Descuento).all()
for row in result:
   for des in row.descuento:
            print (row.id, des.id)

print("Join 2: Trabajador, Descuento")
for c, i in session.query(Trabajador, Descuento) \
    .filter(Trabajador.id == Descuento.id) \
    .all():
    print (f"Id: {c.id} Días Falta: {i.diasFalta}")
print('')

print("Join: Trabajador, Descuento, Bonificacion:")
for c, i, x in session.query(Trabajador, Descuento, Bonificacion) \
    .filter(Trabajador.id == Descuento.id) \
    .filter(Trabajador.id == Bonificacion.id) \
    .all():
   print(f'Id: {c.id} Días de falta: {i.diasFalta} Movilidad: {x.movilidad} ')

print("Saldos Finales:")
for trabajador in trabajadores:
    sueldoBasico = trabajador.sueldoBasico
    bonificaciones = 0

    for bonificacion in trabajador.bonificacion:
        horasExtras = bonificacion.horasExtra
        pagoHorasExtras = 1.50 * horasExtras * sueldoBasico / 30 / 8
        movilidad = bonificacion.movilidad
        bonificacionSuplementaria = 0.03 * sueldoBasico

        bonificaciones += movilidad + bonificacionSuplementaria + pagoHorasExtras

    remuneracionComputable = sueldoBasico + bonificaciones

    descuentoFaltas = 0
    descuentoTardanzas = 0

    for descuento in trabajador.descuento:
        descuentoFaltas += (remuneracionComputable / 30) * int(descuento.diasFalta)
        descuentoTardanzas += (remuneracionComputable / 30 / 8 / 60) * descuento.minutosTardanza

    descuentos = descuentoFaltas + descuentoTardanzas

    SueldoFinal = remuneracionComputable - descuentos

    print(f'Id: {trabajador.id} - Nombre: {trabajador.nombreTrabajador:25} - Sueldo final: {SueldoFinal}')

session.close()
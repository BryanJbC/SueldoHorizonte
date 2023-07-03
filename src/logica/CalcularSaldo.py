from src.modelo.Trabajador import Trabajador
from src.modelo.Bonificacion import Bonificacion
from src.modelo.Descuento import Descuento
from src.modelo.declarative_base import Session

def calcular_saldos_finales():
    session = Session()

    trabajadores = session.query(Trabajador).all()

    saldos_finales = []

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

        sueldo_final = remuneracionComputable - descuentos

        saldo_final = {
            'id': trabajador.id,
            'nombre': trabajador.nombreTrabajador,
            'sueldo_final': sueldo_final
        }

        saldos_finales.append(saldo_final)

    session.close()

    return saldos_finales
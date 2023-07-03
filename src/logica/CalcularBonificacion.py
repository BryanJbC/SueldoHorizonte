from src.modelo.Trabajador import Trabajador
from src.modelo.Bonificacion import Bonificacion
from src.modelo.declarative_base import Session


def calcular_bonificaciones(trabajador):
    sueldoBasico = trabajador.sueldoBasico
    bonificaciones = 0

    for bonificacion in trabajador.bonificacion:
        horasExtras = bonificacion.horasExtra
        pagoHorasExtras = 1.50 * horasExtras * sueldoBasico / 30 / 8
        movilidad = bonificacion.movilidad
        bonificacionSuplementaria = 0.03 * sueldoBasico

        bonificaciones += movilidad + bonificacionSuplementaria + pagoHorasExtras

    return bonificaciones
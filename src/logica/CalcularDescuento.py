from src.modelo.Trabajador import Trabajador
from src.modelo.Bonificacion import Bonificacion
from src.modelo.Descuento import Descuento
from src.modelo.declarative_base import Session
from src.logica.CalcularBonificacion import calcular_bonificaciones

def calcular_descuentos(session, trabajador):
    descuentoFaltas = 0
    descuentoTardanzas = 0

    for descuento in trabajador.descuento:
        remuneracionComputable = trabajador.sueldoBasico + calcular_bonificaciones(trabajador)

        descuentoFaltas += round((remuneracionComputable / 30) * int(descuento.diasFalta), 2)
        descuentoTardanzas += round((remuneracionComputable / 30 / 8 / 60) * descuento.minutosTardanza, 2)

    descuentos = round(descuentoFaltas + descuentoTardanzas, 2)

    return descuentos
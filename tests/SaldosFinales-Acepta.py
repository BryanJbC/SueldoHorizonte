import unittest
from datetime import date
from src.modelo.Trabajador import Trabajador
from src.modelo.Bonificacion import Bonificacion
from src.modelo.Descuento import Descuento
from src.modelo.declarative_base import Session, Base, engine
from src.logica.CalcularSaldo import calcular_saldos_finales

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# create a new session
session = Session()

class TestCalcularSaldosFinales(unittest.TestCase):
    def setUp(self):
        self.session = Session()

    def tearDown(self):
        self.session.query(Descuento).delete()
        self.session.query(Bonificacion).delete()
        self.session.query(Trabajador).delete()
        self.session.commit()
        self.session.close()

    def test_calcular_saldos_finales(self):
        trabajador1 = Trabajador("ene2023", "Juan Matos Solis", 3500)
        trabajador2 = Trabajador("ene2023", "Fernando Salva Ortega", 3000)
        trabajador3 = Trabajador("ene2023", "Manuel Taza Castro", 5000)
        trabajador4 = Trabajador("ene2023", "José Perales Romero", 2500)
        self.session.add(trabajador1)
        self.session.add(trabajador2)
        self.session.add(trabajador3)
        self.session.add(trabajador4)

        descuento1 = Descuento(date(2023, 1, 2), 1, 10, trabajador1)
        descuento2 = Descuento(date(2023, 1, 3), 1, 15, trabajador2)
        descuento3 = Descuento(date(2023, 1, 2), 2, 10, trabajador3)
        self.session.add(descuento1)
        self.session.add(descuento2)
        self.session.add(descuento3)

        bonificacion1 = Bonificacion(date(2023, 1, 1), 4, 1000, trabajador1)
        bonificacion2 = Bonificacion(date(2023, 1, 1), 8, 1000, trabajador2)
        bonificacion3 = Bonificacion(date(2023, 1, 1), 0, 1000, trabajador3)
        bonificacion4 = Bonificacion(date(2023, 1, 1), 2, 1000, trabajador4)
        self.session.add(bonificacion1)
        self.session.add(bonificacion2)
        self.session.add(bonificacion3)
        self.session.add(bonificacion4)

        self.session.commit()

        saldos_finales = calcular_saldos_finales()

        # Verificar los saldos finales esperados
        self.assertEqual(len(saldos_finales), 4)

        self.assertEqual(saldos_finales[0]['id'], trabajador1.id)
        self.assertEqual(saldos_finales[0]['nombre'], trabajador1.nombreTrabajador)
        self.assertAlmostEqual(saldos_finales[0]['sueldo_final'], 4532.82)

        self.assertEqual(saldos_finales[1]['id'], trabajador2.id)
        self.assertEqual(saldos_finales[1]['nombre'], trabajador2.nombreTrabajador)
        self.assertAlmostEqual(saldos_finales[1]['sueldo_final'], 4094.25)

        self.assertEqual(saldos_finales[2]['id'], trabajador3.id)
        self.assertEqual(saldos_finales[2]['nombre'], trabajador3.nombreTrabajador)
        self.assertAlmostEqual(saldos_finales[2]['sueldo_final'], 5735.73)

        self.assertEqual(saldos_finales[3]['id'], trabajador4.id)
        self.assertEqual(saldos_finales[3]['nombre'], trabajador4.nombreTrabajador)
        self.assertAlmostEqual(saldos_finales[3]['sueldo_final'], 3606.25)

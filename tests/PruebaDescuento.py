import unittest
from datetime import date
from src.modelo.Trabajador import Trabajador
from src.modelo.Bonificacion import Bonificacion
from src.modelo.Descuento import Descuento
from src.modelo.declarative_base import Base, engine, Session
from src.logica.CalcularBonificacion import calcular_bonificaciones
from src.logica.CalcularDescuento import calcular_descuentos


class TestCalculoDescuento(unittest.TestCase):

    def setUp(self):
        # Generate database schema
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

        # create a new session
        self.session = Session()

        # create trabajadores
        self.trabajador1 = Trabajador("ene2023", "Juan Matos Solis", 3500)
        self.trabajador2 = Trabajador("ene2023", "Fernando Salva Ortega", 3000)
        self.trabajador3 = Trabajador("ene2023", "Manuel Taza Castro", 5000)
        self.trabajador4 = Trabajador("ene2023", "José Perales Romero", 2500)
        self.session.add(self.trabajador1)
        self.session.add(self.trabajador2)
        self.session.add(self.trabajador3)
        self.session.add(self.trabajador4)

        # create descuentos
        descuento1 = Descuento(date(2023, 1, 2), 1, 10, self.trabajador1)
        descuento2 = Descuento(date(2023, 1, 3), 1, 15, self.trabajador2)
        descuento3 = Descuento(date(2023, 1, 2), 2, 10, self.trabajador3)
        self.session.add(descuento1)
        self.session.add(descuento2)
        self.session.add(descuento3)

        # create bonificaciones
        bonificacion1 = Bonificacion(date(2023, 1, 1), 4, 1000, self.trabajador1)
        bonificacion2 = Bonificacion(date(2023, 1, 1), 8, 1000, self.trabajador2)
        bonificacion3 = Bonificacion(date(2023, 1, 1), 0, 1000, self.trabajador3)
        bonificacion4 = Bonificacion(date(2023, 1, 1), 2, 1000, self.trabajador4)
        self.session.add(bonificacion1)
        self.session.add(bonificacion2)
        self.session.add(bonificacion3)
        self.session.add(bonificacion4)

        self.session.commit()

    def tearDown(self):
        # Drop database schema
        Base.metadata.drop_all(engine)
        self.session.close()

    def test_calcular_descuentos(self):
        descuentos1 = calcular_descuentos(self.session, self.trabajador1)
        descuentos2 = calcular_descuentos(self.session, self.trabajador2)
        descuentos3 = calcular_descuentos(self.session, self.trabajador3)
        descuentos4 = calcular_descuentos(self.session, self.trabajador4)

        self.assertEqual(descuentos1, 0)
        self.assertEqual(descuentos2, 45)
        self.assertEqual(descuentos3, 250)
        self.assertEqual(descuentos4, 0)


import unittest
from datetime import date
from src.modelo.Trabajador import Trabajador
from src.modelo.Bonificacion import Bonificacion
from src.modelo.Descuento import Descuento
from src.modelo.declarative_base import Base, engine, Session
from src.logica.CalcularBonificacion import calcular_bonificaciones

class TestCalcularBonificaciones(unittest.TestCase):
    def setUp(self):
        # Generate database schema
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

        # create a new session
        self.session = Session()

        # create trabajador
        self.trabajador1 = Trabajador("ene2023", "Juan Matos Solis", 3500)
        self.trabajador2 = Trabajador("ene2023", "Fernando Salva Ortega", 3000)
        self.trabajador3 = Trabajador("ene2023", "Manuel Taza Castro", 5000)
        self.trabajador4 = Trabajador("ene2023", "José Perales Romero", 2500)
        self.session.add(self.trabajador1)
        self.session.add(self.trabajador2)
        self.session.add(self.trabajador3)
        self.session.add(self.trabajador4)

             # Crea bonificaciones
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
        self.session.close()

    def test_calcular_bonificaciones(self):
        abc = "hola"
        bonificaciones_trabajador1 = calcular_bonificaciones(self.trabajador1)
        bonificaciones_trabajador2 = calcular_bonificaciones(self.trabajador2)
        bonificaciones_trabajador3 = calcular_bonificaciones(self.trabajador3)
        bonificaciones_trabajador4 = calcular_bonificaciones(self.trabajador4)

        self.assertEqual(bonificaciones_trabajador1, 1192.5)
        self.assertEqual(bonificaciones_trabajador2, 1240)
        self.assertEqual(bonificaciones_trabajador3, 1150)
        self.assertEqual(bonificaciones_trabajador4, 1106.25)
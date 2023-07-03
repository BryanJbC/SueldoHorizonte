from datetime import date
from src.modelo.Trabajador import Trabajador
from src.modelo.Bonificacion import Bonificacion
from src.modelo.Descuento import Descuento
from src.modelo.declarative_base import Base, engine, Session

# Generate database schema
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# create a new session
session = Session()

# create trabajador
trabajador1 = Trabajador("ene2023", "Juan Matos Solis", 3500)
trabajador2 = Trabajador("ene2023", "Fernando Salva Ortega", 3000)
trabajador3 = Trabajador("ene2023", "Manuel Taza Castro", 5000)
trabajador4 = Trabajador("ene2023", "José Perales Romero", 2500)
session.add(trabajador1)
session.add(trabajador2)
session.add(trabajador3)
session.add(trabajador4)

# Crea descuentos
descuento1 = Descuento(date(2023, 1, 2), 1, 10, trabajador1)
descuento2 = Descuento(date(2023, 1, 3), 1, 15, trabajador2)
descuento3 = Descuento(date(2023, 1, 2), 2, 10, trabajador3)
session.add(descuento1)
session.add(descuento2)
session.add(descuento3)

# Crea bonificaciones
bonificacion1 = Bonificacion(date(2023, 1, 1), 4, 1000, trabajador1)
bonificacion2 = Bonificacion(date(2023, 1, 1), 8, 1000, trabajador2)
bonificacion3 = Bonificacion(date(2023, 1, 1), 0, 1000, trabajador3)
bonificacion4 = Bonificacion(date(2023, 1, 1), 2, 1000, trabajador4)
session.add(bonificacion1)
session.add(bonificacion2)
session.add(bonificacion3)
session.add(bonificacion4)

session.commit()
session.close()

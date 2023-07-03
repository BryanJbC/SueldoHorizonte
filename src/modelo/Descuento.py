from sqlalchemy import Column, String, Integer, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from src.modelo.declarative_base import Base

class Descuento(Base):
    __tablename__ = 'descuento'

    id = Column(Integer, primary_key=True)
    fecha = Column(Date)
    diasFalta = Column(String)
    minutosTardanza = Column(Float)
    trabajador_id = Column(Integer, ForeignKey('trabajador.id'))
    trabajador = relationship("Trabajador", backref="descuento")

    def __init__(self, fecha, diasFalta, minutosTardanza, trabajador):
        self.fecha = fecha
        self.diasFalta = diasFalta
        self.minutosTardanza = minutosTardanza
        self.trabajador = trabajador
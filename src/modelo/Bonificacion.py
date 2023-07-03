from sqlalchemy import Column, String, Integer, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from src.modelo.declarative_base import Base


class Bonificacion(Base):
    __tablename__ = 'bonificacion'

    id = Column(Integer, primary_key=True)
    fecha = Column(Date)
    horasExtra = Column(Integer)
    movilidad = Column(Float)
    trabajador_id = Column(Integer, ForeignKey('trabajador.id'))
    trabajador = relationship("Trabajador", backref="bonificacion")

    def __init__(self, fecha, horasExtra, movilidad, trabajador,):
        self.fecha = fecha
        self.horasExtra = horasExtra
        self.movilidad = movilidad
        self.trabajador = trabajador
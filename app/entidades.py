from sqlalchemy import Column, Integer, String
from app.base_datos import base_para_entidades

class Mision(base_para_entidades):
    __tablename__ = "misiones"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    destino = Column(String, nullable=False)
    estado = Column(String, nullable=False)

class Nave(base_para_entidades):
    __tablename__ = "naves"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    modelo = Column(String, nullable=False)
    mision_id = Column(Integer, nullable=False)

class DatosDeLaNave(base_para_entidades):
    __tablename__ = "datos_de_la_nave"

    id = Column(Integer, primary_key=True, index=True)
    nave_id = Column(Integer, nullable=False)
    temperatura = Column(Integer, nullable=False)
    bateria = Column(Integer, nullable=False)
    cobertura = Column(Integer, nullable=False)
from pydantic import BaseModel


class MisionCrear(BaseModel):
    nombre: str
    destino: str
    estado: str

class NaveCrear(BaseModel):
    nombre: str
    modelo: str
    mision_id: int

class DatosDeLaNaveCrear(BaseModel):
    nave_id: int
    temperatura: int
    bateria: int
    cobertura: int

class EstadoDeLaNave(BaseModel):
    nave_id: int
    temperatura: int
    bateria: int
    cobertura: int
    estado: str
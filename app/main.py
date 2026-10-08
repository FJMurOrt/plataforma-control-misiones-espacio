from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.base_datos import sesion_base_datos
from app.entidades import Mision, Nave, DatosDeLaNave
from app.validaciones import (
    MisionCrear,
    NaveCrear,
    DatosDeLaNaveCrear,
    EstadoDeLaNave
)

def abrir_sesion_base_datos():
    sesion = sesion_base_datos()
    try:
        yield sesion
    finally:
        sesion.close()

app = FastAPI(
    title="API para el Control de Misiones Espaciales",
    description="API para gestionar y monitorizar misiones espaciales.",
    version="0.1.0"
)

@app.get("/misiones")
def ver_misiones(sesion: Session = Depends(abrir_sesion_base_datos)):
    misiones = sesion.query(Mision).all()

    return misiones

@app.post("/misiones")
def crear_mision(
    datos_mision: MisionCrear,
    sesion: Session = Depends(abrir_sesion_base_datos)
):
    nueva_mision = Mision(
        nombre=datos_mision.nombre,
        destino=datos_mision.destino,
        estado=datos_mision.estado
    )

    sesion.add(nueva_mision)
    sesion.commit()
    sesion.refresh(nueva_mision)

    return nueva_mision

@app.post("/naves")
def crear_nave(
    datos_nave: NaveCrear,
    sesion: Session = Depends(abrir_sesion_base_datos)
):
    nueva_nave = Nave(
        nombre=datos_nave.nombre,
        modelo=datos_nave.modelo,
        mision_id=datos_nave.mision_id
    )

    sesion.add(nueva_nave)
    sesion.commit()
    sesion.refresh(nueva_nave)

    return nueva_nave

@app.post("/datos-nave")
def crear_datos_nave(
    datos_nave: DatosDeLaNaveCrear,
    sesion: Session = Depends(abrir_sesion_base_datos)
):
    nuevos_datos = DatosDeLaNave(
        nave_id=datos_nave.nave_id,
        temperatura=datos_nave.temperatura,
        bateria=datos_nave.bateria,
        cobertura=datos_nave.cobertura
    )

    sesion.add(nuevos_datos)
    sesion.commit()
    sesion.refresh(nuevos_datos)

    return nuevos_datos

def calcular_estado_nave(temperatura, bateria, cobertura):
    estado = "NORMAL"

    if bateria < 20:
        estado = "Batería de la nave baja"
    elif temperatura > 80:
        estado = "Temperatura de la nave alta"
    elif cobertura < 20:
        estado = "Cobertura de señal con la nave baja"

    return estado

@app.get("/naves/{nave_id}/estado", response_model=EstadoDeLaNave)
def ver_estado_nave(
    nave_id: int,
    sesion: Session = Depends(abrir_sesion_base_datos)
):
    datos_nave = (
        sesion.query(DatosDeLaNave)
        .filter(DatosDeLaNave.nave_id == nave_id)
        .order_by(DatosDeLaNave.id.desc())
        .first()
    )

    if datos_nave is None:
        return {
            "nave_id": nave_id,
            "temperatura": 0,
            "bateria": 0,
            "cobertura": 0,
            "estado": "SIN_DATOS"
        }

    estado = calcular_estado_nave(
        temperatura=datos_nave.temperatura,
        bateria=datos_nave.bateria,
        cobertura=datos_nave.cobertura
    )

    return {
        "nave_id": datos_nave.nave_id,
        "temperatura": datos_nave.temperatura,
        "bateria": datos_nave.bateria,
        "cobertura": datos_nave.cobertura,
        "estado": estado
    }

@app.get("/")
def al_iniciar():
    return {
        "mensaje": "La API funciona correctamente"
    }
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

URL_DE_LA_BASE_DE_DATOS = os.getenv(
    "URL_DE_LA_BASE_DE_DATOS",
    "postgresql+psycopg2://usuario_misiones:contraseña_misiones@localhost:5432/control_misiones"
)

conexion_base_datos = create_engine(URL_DE_LA_BASE_DE_DATOS)

sesion_base_datos = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=conexion_base_datos
)

base_para_entidades = declarative_base()

from app.entidades import Mision, Nave, DatosDeLaNave

def crear_tablas():
    base_para_entidades.metadata.create_all(bind=conexion_base_datos)
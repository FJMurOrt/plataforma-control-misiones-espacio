from fastapi import FastAPI

app = FastAPI(
    title="API para el Control de Misiones Espaciales",
    description="API para gestiónar y monitorizar misiones espaciales.",
    version="0.1.0"
)


@app.get("/")
def al_iniciar():
    return {
        "mensaje": "La API funciona correctamente"
    }
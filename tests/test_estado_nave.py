from app.main import calcular_estado_nave

def test_estado_nave_normal():
    estado = calcular_estado_nave(
        temperatura=25,
        bateria=80,
        cobertura=90
    )

    assert estado == "NORMAL"

def test_estado_nave_bateria_baja():
    estado = calcular_estado_nave(
        temperatura=25,
        bateria=15,
        cobertura=90
    )

    assert estado == "Batería de la nave baja"

def test_estado_nave_temperatura_alta():
    estado = calcular_estado_nave(
        temperatura=90,
        bateria=80,
        cobertura=90
    )

    assert estado == "Temperatura de la nave alta"

def test_estado_nave_cobertura_baja():
    estado = calcular_estado_nave(
        temperatura=25,
        bateria=80,
        cobertura=10
    )

    assert estado == "Cobertura de señal con la nave baja"
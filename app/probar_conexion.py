from base_datos import conexion_base_datos, crear_tablas

try:
    conexion_base_datos.connect()
    print("La conexión con PostgreSQL se ha realizado correctamente.")
    crear_tablas()
    print("Las tablas se crearon correctamente.")

except Exception as error:
    print("Se ha producido un error:")
    print(error)
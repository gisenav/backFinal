import componentes.conexion_db as conexion
def traer_todos():
    con=conexion.conexion
    cursor=con.cursor(dictionary=True)
    consulta="select * from datos;"
    cursor.execute(consulta)
    datos=cursor.fetchall()
    con.close()
    return datos

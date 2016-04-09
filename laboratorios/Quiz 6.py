import sqlite3

def tabla():
    try:
        print("BIENVENIDO")
        conexion= sqlite3.connect("C:/Prueba")
        consulta = conexion.cursor()
        sql = """CREATE TABLE db (
         NOMBRE  CHAR(10) NOT NULL,
         APELLIDO  CHAR(10),
         EDAD INT,
         SEXO CHAR(1) )"""

        if (consulta.execute(sql)):
            print("Tabla creada con éxito")

    except Exception:
        print(" ERROR T-T ")

        consulta.close()
        conexion.commit()
        conexion.close()

def ingresar_datos ():

    NOMBRE=input("Introducir nombre")
    APELLIDO=input("Introducir apellido")
    EDAD=input("Introducir edad")

    conexion=sqlite3.connect("C:/Prueba")
    consulta=conexion.cursor()
    argumentos=(NOMBRE,APELLIDO,EDAD)

    sql="""
    INSERT INTO db (NOMBRE,APELLIDO,EDAD)
    VALUES (?,?,?)
    """
    if(consulta.execute(sql,argumentos)):

        print("Se guardo exitosamente" )
    else : print("ERROR T-T")
    consulta.close()

    conexion.commit()
    conexion.close()

if __name__=="__main__":
    tabla()
    ingresar_datos()


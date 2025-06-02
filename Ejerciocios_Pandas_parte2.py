#Crear un sistema que almacene equipos biomédicos, cada equipo tiene información de:
# nombre, marca, ubicación, fecha de calibración ,fecha de mmto ,nombre del proveedor.
#Para ello implementarlo a partir de un dataframe con la información anterior.
import pandas as pd

def agregar_equipo(nombre, marca, ubicacion, fecha_calibracion ,fecha_mmto ,nombre_proveedor,Data):
    nuevo_equipo = {"nombre":[nombre], "marca":[marca], "ubicacion":[ubicacion], "fecha_calibracion":[fecha_calibracion],"fecha_mmto":[fecha_mmto] ,"nombre_proveedor":[nombre_proveedor]}
    Data = pd.concat([Data, pd.DataFrame(nuevo_equipo)])
    return Data


def main():
    DataFrame_equipos = pd.DataFrame(columns=["nombre", "marca", "ubicacion", "fecha_calibracion" ,"fecha_mmto" ,"nombre_proveedor"])
    while True:
        R = int(input("""1. Agregar equipo
2. Ver equipos
R// """))
        if R == 1:
            print("ingrese los siguientes datos")
            nombre = input("Nombre: ")
            marca = input("Marca: ")
            ubicacion = input("Ubicación: ")
            fecha_calibracion = input("Fecha de calibración: ")
            fecha_mmto = input("Fecha de mantenimiento: ")
            nombre_proveedor = input("Nombre del proveedor: ")
            DataFrame_equipos = agregar_equipo(nombre, marca, ubicacion, fecha_calibracion ,fecha_mmto ,nombre_proveedor,DataFrame_equipos)
        elif R == 2:
            print(DataFrame_equipos)
        else:
            print("Valor no disponible")
if __name__ == "__main__":
    main()
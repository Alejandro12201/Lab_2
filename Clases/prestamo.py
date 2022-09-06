from datetime import datetime
from datetime import timedelta
#------------------------------------------------------------------------------

class prestamo:
    file="database/prestamos.csv"
    def __init__(self, nombre, carnet, equipo, fechap, fechae):
        self.nombre=nombre
        self.carnet=carnet
        self.equipo=equipo
        self.fechap=fechap
        self.fechae=fechae
    #-----------------------------------------------  
       
    def save_prestamo(self):
        f=open(self.file,"a")
        linea=";".join([self.nombre,self.carnet,self.equipo,self.fechap,self.fechae])
        f.write(linea+"\n")
        f.close()
#------------------------------------------------------------------------------

def crear_prestamo():
    print("Registro de prestamo")
    nombre=input("nombre: ")
    carnet=input("carnet: ")
    equipo=input("equipo: ")
    print("Ingrese la fecha de prestamo")
    d_p=int(input("dia dd:  "))
    m_p=int(input("mes mm:  "))
    y_p=int(input("ano yyyy:  "))
    fechap= datetime(y_p,m_p,d_p).strftime("%Y-%m-%d")
    print("Ingrese la fecha de entrega")
    d_e=int(input("dia dd:  "))
    m_e=int(input("mes mm:  "))
    y_e=int(input("ano yyyy:  "))
    fechae= datetime(y_e,m_e,d_e).strftime("%Y-%m-%d")
    p=prestamo(nombre,carnet,equipo,fechap,fechae)
    return p
#------------------------------------------------------------------------------

def ver_prestamos():
    carnet=input("Ingrese su carnet para consultar prestamo")
    datos=get_all_prestamos()
    datos_0=",".join(datos)
    if carnet in datos_0:
        for e in datos:
            if carnet in e:
                datos=e.split(";")
                print("Nombre: "+datos[0])
                print("Carnet: "+datos[1])
                print("Equipo: "+datos[2])
                print("Fecha de prestamo: "+datos[3])
                print("Fecha de entrega: "+datos[4])
    else:
        print("Carnet no registrado, intente de nuevo")
        ver_prestamos()
#------------------------------------------------------------------------------ 

def get_all_prestamos():
    a=open("database/prestamos.csv","r")
    datos=a.readlines()
    return datos
#------------------------------------------------------------------------------ 

def registro_entrega():
    datos=get_all_prestamos()
    carnet=input("Ingrese carnet de estudiante: ")
    equipo=input("Ingrese equipo devuelto: ")
    for e in datos:
        if equipo in e:
            if carnet in e:
                datos.remove(e)
            else:
                print("Prestamo no registrado en la base de datos")
    save_all_prestamo(datos)
#------------------------------------------------------------------------------ 

def save_all_prestamo(datos):
    a=open("database/prestamos.csv","w")
    for e in datos:
        a.write(e)
    a.close()

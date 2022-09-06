#from tabulate import tabulate
from datetime import datetime
from datetime import timedelta
#------------------------------------------------------------------------------

class equipo:
    file="database/equipos.csv"
    def __init__(self,nombre,referencia,proveedor,ciclo,fum,cantidad):
        self.nombre =nombre
        self.referencia= referencia
        self.proveedor= proveedor
        self.ciclo= ciclo 
        self.fum=fum
        self.cantidad=cantidad
    #-----------------------------------------------    
         
    def save_new_equipo(self):
        f=open(self.file,"a")
        linea=";".join([self.nombre,self.referencia,self.proveedor,self.ciclo,self.fum,self.cantidad])
        f.write(linea+"\n")
        f.close()
#------------------------------------------------------------------------------

def crear_equipo():
    print("Registrar nuevo equipo")
    print("")
    nombre=input("Nombre: ")
    referencia=input("referencia: ")
    proveedor=input("Proveedor: ")
    ciclo= input("ciclo de mantenimiento en días: ")
    print("Ingrese la fecha de ultimo mantenimiento: ")
    d_fum=int(input("dia dd:  "))
    m_fum=int(input("mes mm:  "))
    y_fum=int(input("ano yyyy:  "))
    fum= datetime(y_fum,m_fum,d_fum).strftime("%Y-%m-%d")
    cantidad=input("cantidad: ")
    eq = equipo(nombre,referencia,proveedor,ciclo,fum,cantidad)
    return eq
#------------------------------------------------------------------------------

def consultar_equipo():
    print("conculta de equipos")
    nombre=input("nombre del equipo")
    datos=get_all_equipos()
    cantidad=0
    datos_0=",".join(datos)
    if nombre in datos_0:
        for e in datos:
            if nombre in e:
                datos=e.split(";")
                cantidad=int(datos[5])
                if cantidad > 0:
                    print("El equipo existe en la base de datos y hay " + str(cantidad)+ " equipos.")
                else:
                    print("No hay equipos disponibles")
    else:
        print("El  equipo no existe en la base de datos")
    return cantidad
#------------------------------------------------------------------------------

def registro_mantenimiento():
    lista_equipos=get_all_equipos()
    equipo=input("equipo")
    print("Ingrese la fecha de ultimo mantenimiento")
    d_fum=int(input("dia dd:  "))
    m_fum=int(input("mes mm:  "))
    y_fum=int(input("ano yyyy:  "))
    fum= datetime(y_fum,m_fum,d_fum).strftime("%Y-%m-%d")
    pos=0
    for e in lista_equipos:
        if equipo in e:
            datos_equipo=e.split(";")
            datos_equipo[4]=fum
            #datos_equipo[5]=datos_equipo[5]+"\n"
            lista_equipos[pos]=";".join(datos_equipo)
        pos=pos+1
    save_all_equipos(lista_equipos)
#------------------------------------------------------------------------------

def rango_fechas():
    print("Por favor ingrese el rango de fechas que desea consultar")
    print("")
    d_ini=int(input("dia de inicio dd:  "))
    m_ini=int(input("mes de inicio mm:  "))
    y_ini=int(input("ano de inicio yyyy:  "))
    print("")
    d_ter=int(input("dia de finalizacion dd:  "))
    m_ter=int(input("mes de finalizacion mm:  "))
    y_ter=int(input("ano de finalizacion yyyy:  "))    
    print("")   
    start= datetime(y_ini,m_ini,d_ini)
    end= datetime(y_ter,m_ter,d_ter)
    header=[]
    header= [(start + timedelta(days=d)).strftime("%Y-%m-%d")
                        for d in range((end - start).days+1)]
    #print(header)
    datos=get_all_equipos()
    datos_0=",".join(datos)
    #print(datos)
    #print("")
    #print(datos_0)
    #print("")
    fechas=[]
    for e in range(len(header)):
        if header[e] in datos_0:
            fechas.append(header[e])
            #print(header[e])
            #print(e)
    #print(fechas)
    if not fechas:
        print("Ningun equipo se encuentra dentro del rango de fechas de mantenimiento ")
    else:
        for i in range(len(fechas)):
            if fechas[i] in datos_0:
                for e in datos:
                    if fechas[i] in e:
                        datos=e.split(";")
                        print("El equipo: "+datos[0]+" Se encuentra en el rango de fechas de mantenimiento: ")
                        print("Referencia: "+datos[1])
                        print("Proveedor: "+datos[2])
                        print("Ciclo de mantenimiento: "+datos[3]) 
                        print("Fecha de ultimo mantenimiento: "+datos[4])
                        print("Cantidad: "+datos[5])
#------------------------------------------------------------------------------

def save_all_equipos(equipos):
    a=open("database/equipos.csv","w")
    for e in equipos:
        a.write(e)
    a.close()
#------------------------------------------------------------------------------

def get_all_equipos():
    a=open("database/equipos.csv","r")
    datos=a.readlines()
    return datos



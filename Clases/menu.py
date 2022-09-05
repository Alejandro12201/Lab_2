class menu():
  def __init__(self,laboratorio):
    self.laboratorio = laboratorio

  def ver(self):
    print("BIENVENIDO AL SISTEMA".center(50,"*"))
    print("Laboratorio:"+self.laboratorio)
    print("1. Técnicos")
    print("2. Estudiantes")
    op=int(input(">>> "))
    return op

#------------------------------------------------------------------------------
class menu_tecnicos():
    def __init__(self,laboratorio):
        self.laboratorio = laboratorio

    def ver(self):
      print("Menu Tecnicos".center(20,"*"))
      print("Laboratorio:"+self.laboratorio)
      print("1. Registrar equipo")
      print("2. Registrar prestamo")
      print("3. Consulta de equipos en un rango de fechas")
      print("4. Registrar ultima fecha de mantenimiento")
      op=int(input(">>> "))
      return op
      
#------------------------------------------------------------------------------
class menu_estudiantes():
    def __init__(self,laboratorio):
        self.laboratorio = laboratorio

    def ver(self):
      print("Menu Estudiantes".center(20,"*"))
      print("Laboratorio:"+self.laboratorio)
      print("1. Consultar mis equipos en prestamo")
      print("2. Consultar equipos disponibles")
      op=int(input(">>> "))
      return op
      





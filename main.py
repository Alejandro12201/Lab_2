from Clases.menu import *
from Clases.equipo import *
from Clases.prestamo import *
from datetime import datetime
from datetime import timedelta

#------------------------------------------------------------------------------

def main():
    Menu=menu("Escuela colmbiana de ingeniería julio garavito")
    op=Menu.ver()
    if op==1:
        menu2= menu_tecnicos("Ingenieria biomedica")
        op2=menu2.ver()
        if op2==1:
            eq=crear_equipo()
            eq.save_new_equipo()
            main()

        elif op2== 2:
            eq=consultar_equipo()
            if eq>0:
                p=crear_prestamo()
                p.save_prestamo()
                main()
            else:
                main()

        elif op2==3:
            rango_fechas()
            main()
        
        elif op2==4:
            eq=consultar_equipo()
            if eq>0:
                registro_mantenimiento()
                main()
            else:
                main()

        else:
            print("opcion incorrecta")
            main()

    elif op==2:
        menu2=menu_estudiantes("Ingenieria biomedica")
        op2=menu2.ver()
        if op2==1:
            ver_prestamos()
            main()

        elif op2==2:
            consultar_equipo()
            main()
        
        else:
            print("Opcion incorrecta, por favor intente de nuevo")
            main()

    else:
        print("opcion incorrecta, por favor intente de nuevo")
        main()
        
if __name__=='__main__':
    main()
    
    
    
    
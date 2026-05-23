
"""
  Una función es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa mas pequeño que cumple una funcion especifica. La funcion se puede reutulizar con el simple hecho de invocarla es decir mandarla llamar 

  Sintaxis:

   def nombredeMifuncion(parametros):
      bloque o conjunto de instrucciones

   nombredeMifuncion(parametros)

   Las funciones pueden ser de 4 tipos
  
    Funciones de tipo "Procedimiento" 
   1.- Funcion que no recibe parametros y no regresa valor
   3.- Funcion que recibe parametros y no regresa valor
    
    Funciones de tipo "Funcion"
   2.- Funcion que no recibe parametros y regresa valor
   4.- Funcion que recibe parametros y regresa valor

"""
#1.- Funcion que no recibe parametros y no regresa valor
def funcion1():
    nombre=input("Ingresa el nombre: ").upper().strip()
    apellido=input("Apellido: ").upper().strip()
    print(f"El nombre del alumno es:{nombre}{apellido}")


 #3.- Funcion que recibe parametros y no regresa valor
def funcion3(nom,ape):
    nombre=nom
    apellido=ape
    print(f"El nombre del alumno es:{nombre}{apellido}") 


 #2.- Funcion que no recibe parametros y regresa valor
def funcion2():
    nombre=input("Ingresa el nombre: ").upper().strip()
    apellido=input("Apellido: ").upper().strip()
    print(f"El nombre del alumno es:{nombre}{apellido}")
    return nombre,apellido

 #4.- Funcion que recibe parametros y regresa valor

def funcion4(nom,ape):
    nombre=nom
    apellido=ape
    return nombre,apellido

#Invocar las funciones

funcion1()
#--------
nombre=input("Ingresa el nombre: ").upper().strip()
apellido=input("Apellido: ").upper().strip()
funcion3(nombre,apellido)
#--------------
nombre,apellido=funcion2()
print(f"El nombre del alumno es:{nombre}{apellido}")


nom=input("Ingresa el nombre: ").upper().strip()
ape=input("Apellido: ").upper().strip()
nombre,apellido=funcion4(nom,ape)
print(f"El nombre del alumno es:{nombre}{apellido}")



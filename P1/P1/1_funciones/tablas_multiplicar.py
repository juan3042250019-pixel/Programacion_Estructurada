'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Sin estructuras de control
  2.- Sin funciones


'''
print("\033c")

num_Tabla=int(input("dame un numero para obtener la tabla de multiplicar: "))
num=1

multi=num_Tabla*num
print(f"{num_Tabla}X{num}={multi}")
num+=1
multi=num_Tabla*num
print(f"{num_Tabla}X{num}={multi}")
num+=1
multi=num_Tabla*num
print(f"{num_Tabla}X{num}={multi}")
num+=1
multi=num_Tabla*num
print(f"{num_Tabla}X{num}={multi}")
num+=1
multi=num_Tabla*num
print(f"{num_Tabla}X{num}={multi}")
num+=1
multi=num_Tabla*num
print(f"{num_Tabla}X{num}={multi}")
num+=1
multi=num_Tabla*num
print(f"{num_Tabla}X{num}={multi}")
num+=1
multi=num_Tabla*num
print(f"{num_Tabla}X{num}={multi}")
num+=1
multi=num_Tabla*num
print(f"{num_Tabla}X{num}={multi}")
num+=1
multi=num_Tabla*num
print(f"{num_Tabla}X{num}={multi}")
num+=1

'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- con estructuras de control  con for 
  2.- Sin funciones
'''


print("\033c")
num1_Tabla=int(input("dame un numero para obtener la tabla de multiplicar: "))

for i in range(1,11):
      multi=num1_Tabla*i
      print(f"{num1_Tabla}X{i}={multi}")
   


i=1
while i<=10:
     multi=num1_Tabla*i
     print(f"{num1_Tabla}X{i}={multi}")
     i+=1


'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- con estructuras de control for con decremento de 10
  2.- Sin funciones

'''
num = 1
for i in range(100, 0, -10):
    multi = num1_Tabla * i
    print(f"{num1_Tabla} X {i} = {multi} ")
    num += 1

i = 100
while i > 0:
    multi = num1_Tabla * i
    print(f"{num1_Tabla} X {i} = {multi} ")
    i -= 10

'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- sin estructuras de control 
  2.- con funciones

'''


def multiplicar(num_tabla, n):
    multi = num_tabla * n
    print(f"{n} X {num_tabla} = {multi} ")
    n += 1
    return n


num_tabla = int(input("Ingresa un numero: "))
num = 1

num = multiplicar(num_tabla, num)
num = multiplicar(num_tabla, num)
num = multiplicar(num_tabla, num)
num = multiplicar(num_tabla, num)
num = multiplicar(num_tabla, num)
num = multiplicar(num_tabla, num)
num = multiplicar(num_tabla, num)
num = multiplicar(num_tabla, num)
num = multiplicar(num_tabla, num)
num = multiplicar(num_tabla, num)

'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- con estructuras de control 
  2.- con funciones

'''


def multiplicar(num_tabla, n):
    for i in range(1, 11):
        multi = num_tabla * n
        print(f"{n} X {num_tabla} = {multi} ")
        n += 1
    return n


num_tabla = int(input("Ingresa un numero con: "))
n = 1
multiplicar(num_tabla, n)





      
    
    

import funciones  

def menuPrincial():
    print("\n\t\t...:::: M E N U  P R I N C I P A L ::::...\n")
    opcion=input("\n\t1.- Agregar\n\t2.- Borrar\n\t3.- Modificar\n\t4.- Mostrar\n\t5.- Buscar\n\t6.- Limpiar\n\t7.- Salir\n\t\tEscribe un opcion: ").strip()
    return opcion

def agregarPeliculas(pelis):
    print("\n\t\t...:::: AGREGAR CARACTERISTICAS DE UNA PELICULA ::::...\n")
    caracteristica=input("Introduce el nombre de la caracterisrica: ").lower().strip()
    valor=input("Introduce el valor de la caracterisrica: ").upper().strip()
    # pelis.append(peli)
    pelis[caracteristica]=valor
    funciones.accionExitosa()

def mostrarPeliculas(pelis):
    print("\n\t\t...:::: MOSTRAR LAS CARACTERISTICAS DE LA PELICULA ::::...\n")
    if len(pelis)>0:
        print("\tCaracteristica\t\tValor\n")
        for i in pelis:
            print(f"{i}\t\t{pelis[i]}")
        funciones.espereTecla()
    else:
        print("\n\t\t...:::: no hay caracteristicas para mostrar ::::...\n")

    
def limpiarPeliculas(pelis):
    if len(pelis)>0:
        opc=""
        while opc!="si" and opc!="no":
                    opc=input("¿Deseas borrar todas las pelicula (Si/No)? ").lower().strip()
        if opc=="si":
            pelis.clear()
            funciones.accionExitosa()
    else:
        input("...¡No hay peliculas que borrar!...") 
        
def buscarPeliculas(pelis):
    print("\n\t\t...:::: BUSCAR UNA CARACTERISTICA DE LA PELICULA ::::...\n")
    caracteristica=input("Escribe el nombre de la caracteristica ").upper().strip()
    
    no_encontro=True
    for i in pelis:
        if caracteristica==i:
            no_encontro=False
            print("\tCaracteristica\t\tValor\n")
            print(f"{i+1}\t\t{pelis[i]}")
            funciones.espereTecla()
        if no_encontro:
            input("...¡No exite la pelicula que estas buscando, verifique!...")

        
            

def borrarPeliculas(pelis):
    print("\n\t\t...:::: BORRAR CARACTERISTICA DE UNA PELICULA ::::...\n")
    caracteristica=input("Escribe el nombre de la caracteristica: ").lower().strip()
    no_encontro = True
    for i in pelis:
        if caracteristica==i:
            opc=""
            while opc!="si" and opc!="no":
                opc=input("¿Deseas borrar la pelicula (Si/No)? ").lower().strip()
            if opc=="si":
                pelis.pop(caracteristica)
                no_encontro=False
                funciones.accionExitosa()
    if no_encontro:
        input("...¡No exite la caracteristica de la pelicula que estas buscando, verifique!...")
        
def modificarPeliculas(pelis):
    print("\n\t\t...:::: MODIFICAR EL VALOR DE LA CARACTERISTICA ::::...\n")
    caracteristica=input("Escribe el nombre de la caracteristica: ").lower().strip()
    no_encontro=True
    for i in pelis:
        if caracteristica==i:
            print("\tCaracteristica\t\tValor\n")
            print(f"{i}\t\t{pelis[i]}")
            opc=""
            while opc!="si" and opc!="no":
                for i in pelis:
                    opc=input("¿Deseas modificar el valor de la caracteristica de la pelicula (Si/No)? ").lower().strip()
            if opc=="si":
                pelis[caracteristica]=input("Escribe el nuevo valor de la caracteristica: ").lower().strip()
                no_encontro= False
                funciones.accionExitosa()
    if no_encontro:
        input("...¡No exite la caracteristica de la pelicula que estas buscando, verifique!...")
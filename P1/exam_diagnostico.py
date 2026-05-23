def borrarPantalla():
    print("\033c")

def ventaAutos(opcion,contador,total):
    borrarPantalla()

    opcion="s"

    while opcion=="s":
        
        marca=input("Ingresa la marca del carro ")
        origen=input("Ingresa el origen del carro ").lower()
        costo=float(input("Ingresa el costo del carro "))
        
        impuesto=0
        contador=0
        total=0

        if origen=="americano":
            impuesto=costo*0.20
            
        elif origen=="alemania":
            impuesto=costo*0.30
            
        elif origen=="japon":
            impuesto=costo*0.25   
            

        total+=costo+impuesto
        contador+=1

        opcion=input("¿Desea agregar otro carro? (s/n)").lower().strip()

    return contador,total

OPC="S"
AUTOS=0
ACUM_PV=0


tot_autos,acum_precios=ventaAutos(OPC,AUTOS,ACUM_PV)         
print(f"el total de los carros es:{tot_autos} y el total de la venta de todos los carros es:{acum_precios}")






                







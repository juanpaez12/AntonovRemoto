pa = 0
d=float(input("Ingrese la distancia a recorrer: "))
v=int(input("Escoja un tipo de vuelo: Nacional(1) o Internacional(2) "))

while not(v==1) and not(v==2) :
    v=int(input("Escoja 1 o 2 "))

np=0

#p es el peso, vd el precio a cobrar de la distancia, vp el valor a cobrar del peso y vd es el valor total del envio
#El peso recomendando que puede llevar un Antonov es del 95% de su capacidad que equivale a 337250 y su capaxima maxima de trasnporte es de 355000. Una vez supere el 95% se debe dejar de cargar. 
while pa<=337250 :
    p=float(input("Ingrese el peso del producto en kilogramos: "))
    if p>10 :
        pa=pa+p
        if pa<=355000 :   
            if v==1 :
                vd=4000*d
                vp=4500*p
                vt=vd+vp
                if p>100 :
                    vt=vt*0.85
            elif v==2:
                vd=8000*d
                vp=4500*p
                vt=vd+vp
                if p>400 and d>8000 :
                    vt=vt*0.90
            print("El valor total es: " + str(vt))
        else : 
            print("El paquete supera el límite de peso")
            pa=pa-p
    else :
        print("El peso de su producto no es aceptado")
    np=np+1    
    
    d=float(input("Ingrese una nueva distancia: "))
    v=int(input("Escoja un tipo de vuelo: Nacional(1) o Internacional(2) "))

    while v!=1 and v!=2:
        v=int(input("Escoja 1 o 2 "))
        
print("Avion con carga maxima y listo para despegar")
print("El peso de los paquetes es: " + str(pa))   
print("El numero de productos es: " +str(np))
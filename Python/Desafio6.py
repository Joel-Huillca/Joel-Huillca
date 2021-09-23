# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 17:11:38 2017

@author: 
"""
print("Bienvenido!")



Ancho = []
Alto  = []
Punto=[]
continuar = "S"
cantP=0

while continuar == "S":
    Puntos = 0
    print("Para terminar de obtener datos, ingrese una cantidad de habitaciones igual a cero")
    cantH = int(input("Ingrese la cantidad de habitaciones de la propiedad que desea evaluar: "))
    if cantH != 0 and cantH > 0:
        for a in range(cantH):
            AnchH = int(input("Ingrese el Ancho de la habitación: "))
            Ancho.append(AnchH)
            
            AltH = int(input(" Ingrese el Alto de la habitación: "))
            Alto.append(AltH)
            
        Areas = []
        
        for i in range(cantH):
            Area= Ancho[i] * Alto[i]
            Areas.append(Area)
            Area = 0

        sumaArea=0
        for i in Areas:
            sumaArea += i
        
   
        print("El area total construida es de: ", sumaArea)
        
        if sumaArea > 200:
            Puntos += 15
        elif sumaArea <= 200 and sumaArea > 100:
            Puntos += 5
        else:
            Puntos = 0
    
        AreaT = int(input("Ingrese el area total de la propiedad: "))
    
        porc= (sumaArea*100)/AreaT
    
        if porc < 50:
            Puntos += 5
            if sumaArea > 200:
                Puntos += 10
        
            piscina = ""
            while piscina != "S" and piscina != "N":
                piscina= input("La propiedad tiene piscina?(S/N): ")
                if piscina == "S":
                    Puntos += 5
        
            asados = ""
            while asados != "S" and asados != "N":
                asados= input("tiene lugar para asados?(S/N): ")
                if asados == "S":
                    Puntos += 5
        
            if piscina == "S" and asados == "S":
                Puntos += 5
            
        distC = int(input("Cual es la distancia al colegio mas cercano? "))
    
        if distC <= 3000:
            Puntos += 5
        
        elif distC > 3000 and distC < 1000:
            Puntos += 2
    
        elif distC >= 10000:
            Puntos -= 2
        
        CantS = int(input("Cantidad de supermercados cerca: "))
    
        if CantS > 2:
            Puntos += 5
        elif CantS <= 2 and CantS >= 1:
            Puntos += 2
        elif CantS == 0:
            Puntos -= 5
        
        if distC <= 3000 and CantS > 2:
            Puntos += 5
        
        Punto.append(Puntos)
        
        print("El puntaje total de la propiedad es", Puntos)
        
        continuar = ""
        while continuar != "S" and continuar != "N":
            continuar = input("Desea evaluar otra propiedad?(S/N): ")
            if continuar == "S":
                Ancho.clear()
                Alto.clear()
                cantP += 1
    else:
        print("No se han ingresado habitaciones, por lo tanto la recopilacion de datos termina")
        continuar = "N"
        
for a in range(cantP+1):
    if Punto[a] > 40:
        print("La propiedad", str(a+1),"obtuvo", Punto[a], "puntos", "Y se recomienda su compra")
    else:
        print("La propiedad", str(a+1),"obtuvo", Punto[a], "puntos")

print("La mejor evaluada fue la propiedad", Punto.index(max(Punto))+1)




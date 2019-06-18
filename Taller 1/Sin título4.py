# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 06:59:03 2019

@author: David Madroñero F
"""
#Taller 4 punto
#el usuario introduce el valor del numero
Entero1=(int(input('introduzca el entero de su preferencia: ')))
X=[] #X es un alista vacia de elemntos 
Entero1=abs(Entero1)# valor absoluto del número
#establecida la condición si el entero introducido por el usuario es mayor o 
#igual a 10.
while (Entero1>=10):
    resultado=Entero1%10
    X.append(resultado)
    Entero1=Entero1//10
#append me agregara el valor del Entero1 a la lista (X)
X.append(Entero1)
Y=[]
for i in range (0,len(X)):
    Y.append(X[-i-1])
#El programa solo sumara los número pares que esten entre el intervalo de 
    #0,len(x)
print(Y)
sumapares=0
for i in range (0,len(Y)):
    if Y[i]%2==0:
        sumapares=Y[i]+sumapares
        
print(sumapares) #impresion de la suma de los nímeros parares de la lista
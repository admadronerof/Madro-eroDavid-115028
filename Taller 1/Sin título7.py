# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 09:12:00 2019

@author: David Madroñero F
"""

Entero1=(int(input('introduzca el número que quiera: ')))
Lista1=[]
Entero1=abs(Entero1)
while (Entero1>=10): #para números mayores o iguales a 10
    Resultado=Entero1%10 #parte entera del cociente
    Lista1.append(Resultado)
    Entero1=Entero1//103#Se eliminan los decimales del número
Lista1.append(Entero1)# se introduce el valor del entero 1 en la lista
#se crea una lista 2
Lista2=[]
#bajo la condicion de para i en el rago de 
for i in range (0,len(Lista1)):
    Lista2.append(Lista1[-i-1])
  
Lista3=[]
for i in range (0,len(Lista2)):
    for j in range(i+1,len(Lista2)):
        if Lista2[i]==Lista2[j]:
            Lista3.append(Lista2[i])
            
for i in range(0,len(Lista3)):
    for j in range(i+1,len(Lista3)):
        if Lista3[i]==Lista3[j]:
            Lista3[j]='Lista1'
            
Lista4=[]
for i in range(0,len(Lista3)):
    if Lista3[i]!='Lista1':
        Lista4.append(Lista3[i])
    
print(Lista4)
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 03:02:39 2019

@author: David Madroñero F
"""
#Taller punto 4

Entero1=(int(input('introduzca su número entero: ')))
Lista1=[]
Entero1=abs(Entero1)
#condicion si el entero es mayor o igual a 10 
while (Entero1>=10): 
    resultado=Entero1%10     # variable resultado toma el valor de Entero%10
    Lista1.append(resultado) #append me agregara el resultado al fina de lista
                             #en este caso el resultado
    Entero1=Entero1//10 
    
Lista1.append(Entero1)
Lista2=[]
for i in range (0,len(Lista1)):
    Lista2.append(Lista1[-i-1])
    
print(Lista2)
sumapares=0
for i in range (0,len(Lista2)):
    if Lista2[i]%2==0:
        sumapares=Lista2[i]+sumapares
        
print(sumapares)
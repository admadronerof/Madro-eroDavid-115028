# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 04:32:38 2019

@author: David Madroñero F
"""

Entero1=(int(input('introduzca el varlor que desea: ')))
Lista1=[]
Entero1=abs(Entero1) #valor absoluto del número indicado 
while (Entero1>=10): #si Entero1>=10, se ejecuta while, append me introducira
                     # el valor del Entero1, en la Lista
    x=Entero1%10
    Lista1.append(x)
    Entero1=Entero1//10
Lista1.append(Entero1)

Lista2=[]

for i in range (0,len(Lista1)):
    Lista2.append(Lista1[-i-1])
y=0
Lista3=[]    
for i in range (0,len(Lista2)):
    if Lista2[i]==5:
        y=y+1
        if i==len(Lista2)-1:
            Lista3.append(y)
    else:
        if y !=0:
            Lista3.append(y)
            y=0
            
print(Lista3)          

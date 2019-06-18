# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 07:23:01 2019

@author: David Madroñero F
"""

Entero1=(int(input('Introduz el número que dese: ')))
Lista1=[]
Entero1=abs(Entero1)
while (Entero1>=10): #para números mayores o iguales a 10
    Resultado=Entero1%10 #la parte entera del cociente
    Lista1.append(Resultado)
    Entero1=Entero1//10 #se eliminan los decimales del número
Lista1.append(Entero1) # se introduce el valor en la lista

Lista2=[] #se crea un nueva lista
x=0
for i in range (0,len(Lista1)):
    Lista2.append(Lista1[-i-1]) #para que el número se lea derecha a izquierda
    x=Lista2[i]+x
print('suma de los digitos',x)
#se establecen dos variables como fibonacci1=0
# y fibonacci=1, dado que son numeroes que pertencen a la serie de finonacci   
fibonacci1=0
fibonacci2=1
#la serie de fibonacci se trata de una sucesión infinita de números naturales
#que comienza 1 y cada termino se obtiene sumando los dos anteriores 
for i in range(0,100000):
    fibonacci2=fibonacci1+fibonacci2
    fibonacci1=fibonacci2-fibonacci1
 
    if fibonacci2==x:
        print('la suma de los dos digitos esta en la lista de fibonacci')
        break
    if fibonacci2>x:
        print('la suma de los dos digitos no esta en la lista de fibonacci')
        break   
if Entero1==0:
     print('la suma de los dos digitos esta en la lista de fibonacci')
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 09:41:31 2019

@author: David Madroñero F
"""
#Taller punto 2

Entero1=(int(input('digite el numero: ')))
Espacio=[] #deja el espacio en la lista para furutos valores
contenido=0
#se establece la condicón que sean valores maypres o iguales 10 dado 
#que el programa me tiene que votar el número en reversa, siendo 10 
#El minimo valor que puede tomar el Entero1.
while(Entero1>=10): 
    resultado=Entero1%10
    #el comando append me agrega el resulda al minal de mi lista.
    Espacio.append(resultado)
    Entero1=Entero1//10
    contenido=contenido+1
    print(contenido)
#hasta este punto el programa solo me dara una lista de los numero escogidos
#con append al espacio estoy agregando el entero1 al final de mi lista
Espacio.append(Entero1)
print (contenido)
Entero2=0
for i in range (0,contenido+1):
    print(i)
    Entero2=Espacio[i]*10**(contenido-i)+Entero2
print(Entero2)
    
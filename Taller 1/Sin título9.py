# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 10:20:53 2019

@author: David Madroñero F
"""
#Taller punto 9

import math
#se establecen las coordenadas de x y y r para estableser el primer circulo
x1=(int(input('(primer circulo)introduzca la coordenada en x: ')))
y1=(int(input('(primer circulo)introduzca la coordenada en y: ')))
r1=(int(input('(primer circulo)introduzca el radio: ')))
#se establecen las coordenadas de x y y r para estableser el srgundo circulo
x2=(int(input('(segundo circulo)introduzca la coordenada en x: ')))
y2=(int(input('(segundo circulo)introduzca la coordenada en y: ')))
r2=(int(input('(segundo circulo)introduzca el radio: ')))
#coordenadas del punto 
a=(int(input('coord en a: ')))
b=(int(input('coord en b: ')))

dist1=math.sqrt((x1-a)**2+(y1-b)**2)
dist2=math.sqrt((x2-a)**2+(y2-b)**2)
# se establecen las condiciones para saber si el punto esta dentro,fuera
#dentro de ambos o fuera de ambos 
C=0
if (dist1<=r1): #si la distancia1 es menor al radio1
    print('(a,b) esta en el circulo 1')
    C=C+1
else: #si la distancia1 no es menor al radio1 quiere decir que esta fuera
    print('(a,b) no esta en el circulo 1')
if (dist2<=r2): #si la distancia2 es menor al radio2
    print('(a,b) esta en el circulo 2')
    C=C+1
else: #si la distancia2 no es menor al radio1 quiere decir que esta fuera
    print('(a,b) no esta en el circulo 2')
if (C==2):
    print('(a,b) esta en los dos circulos')
if (C==0):
    print('(a,b) no esta en ninguno de los dos circulos')

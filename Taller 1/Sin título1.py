# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 04:09:27 2019

@author: David Madroñero F
"""
# Taller punto 1
import math
#se pide al usuario digitar cualquier número 
numero=(float(input('digite el valor del numero entero o decimal: ' )))
#se eleva el numero al cuadrado y se le saca la raiz, esto hace los
#número negativos positivos.
numero=math.sqrt(numero**2)
print('valor absoluto: ', numero)
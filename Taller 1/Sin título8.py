# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 09:55:45 2019

@author: David Madroñero F
"""

#Taller punto 8
A=0
#se establece la condición para i en el rango de 1 a 100
for i in range(1,100):
# si A<=15 los primeros 15 digitos son multiplos de 3
    if A<= 15:        
        x = i%3
        
        if x == 0:            
            A=A+1
            
            print('para este número',i,'es multiplo de 3')
# si no es el caso los siguientes digitios despues del 15 son multiplos de 4    
    else:        
        y = i%4;
        
        if y == 0:                
            print('este otro número',i,'multiplo de 4 ')
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Tabla de la verdad

# Tabla de verdad and
print(True and True)
print(True and False)
print(False and False)
print(False and False)

# Tabla de verdad or
print(True and True)
print(True and False)
print(False and False)
print(False and False)

# Negacion

print(not True)
print(not False)

print(True and False and True )

print(True and (False and True)
      or False or (True or True)
      )

# Estructura if

x = 6
if (x > 0):
    print('1')
else:
    print('2')
print('3')


if x > 0:
    print('Mayor que cero')
elif x == 0:
    print('Es igual a cero')
else:
    print('Entro aqui')
    

# dada la edad de una persona diga si es mayor o menor de edad

edad = int(input('Ingrese su edad: \n'))

if edad >= 18:
    print('Es mayor de edad')
else:
    print('Es menor de edad')
    

# 

calificacion = float(input('Ingrese la calificacion del estudiante: \n'))

if calificacion < 0 or calificacion > 5:
    print('No es una nota valida')
elif calificacion >= 3:
    print('Aprobo')
else:
    print('Reprobo')
    
# 

numero = int(input('ingrese un numero \n'))

if numero < 0:
    print('Es un numero negativo')
elif numero == 0:
    print('El numero es cero')
else:
    print('Es un numero positivo')


    
 # Ciclos 

# Range - Iterador Flojo

for valor in range(4):
    print(valor)
   

for valor in range(1, 6):
    print(valor)
    

for valor in range(1, 100, 2):
    print(valor)
    
 
for i in range(1, 11):
    for j in range(1, 6):
        print(i,j)  
        
# While

while True:
    print('Hola Mundo')
    break

#

notas = 0
numero_notas = int(input('Ingrese el numero de notas'))    
for i in range(1, numero_notas + 1):
    while True:
        nota = float(input(f'Ingrese la nota numero {i}'))
        if nota <5 and nota >0:
            break
        notas = notas + nota
promedio = notas / numero_notas
print(f'El promedio dinal de las notas {numero_notas} notas es:', promedio)

# Tipos de colecciones

# Listas o vectores
# Tipo de dato mutable y ordenado

a = [2, 3, 4]
b = [2, True, 'Hola', 3.4]
c = [2, [True, False], ['Hola', 'Mundo'], [2.3, 3.4, 4.6, 7.8]]

for var in c:
    print(var)
    
    
    
    
    
    
    
    
    
    
    


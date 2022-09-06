"""Escribe un programa que pida un número entero de tres dígitos.
Si el número recibido tiene tres dígitos, que calcule la suma del cuadrado de sus dígitos
De lo contrario, que imprima un mensaje que diga que el número recibido no es de tres dígitos.
Fácil ¿no?

Tips para saber si un número tiene tres dígitos: si el número es mayor o igual a 100 y el número es
menor o igual a 999.

Por ejemplo, supongamos que el número recibido es 527, aunque podría ser cualquier otro, es un
número de tres dígitos y sus dígitos son 5, 2 y 7
El cuadrado de 5 es 25
El cuadrado de 2 es 4
El cuadrado de 7 es 49
La suma de 25 + 4 + 49 es 78

O si empezamos por las unidades:
El cuadrado de 7 es 49
El cuadrado de 2 es 4
El cuadrado de 5 es 25
La suma de 49 + 4 + 25 es 78

Tips para separar los dígitos de un número:
numero = 527
unidades = numero % 10 -> 7
numero = numero // 10 -> 52
decenas = numero % 10 -> 2
numero = numero // 10 -> 5
centenas = numero % 10 -> 5 # o simplemente centenas = numero"""

numero =  int(input("Inserte un número de 3 dígitos porfis"))
if numero >= 100 and numero <=999:
    unidades = numero % 10
    numero = numero // 10
    decenas = numero % 10
    numero = numero // 10
    centenas = numero % 10
    print(int(unidades**2 + decenas**2 +centenas**2))

#tipos de datos primitivos

#string

nombre= "Jorge David"

apellido = "González"

#int
edad = 35 

#float
estatura = 1.78

#boolean 
diestro = True

#concatenar variables

variables_concatenadas = "Hola mi nombre es: {} {} tengo {} años  mi estatura es: {} soy diestro {}".format( nombre, apellido, edad, estatura, diestro)

print(variables_concatenadas)

"""
Los números enteros y los números flotantes son dos tipos de datos numéricos en Python.\n
Los números enteros son aquellos que no tienen parte decimal, como 1, 2, 3, etc. \n
Los números flotantes son aquellos que tienen parte decimal, como 0.1, 3.14, 6.28, etc.

Los números enteros en Python 3 no tienen un límite de tamaño, por lo que pueden representar \n
cualquier valor entero que se pueda almacenar en la memoria de la computadora. Los números \n 
flotantes en Python tienen una precisión de 15 posiciones decimales, lo que significa que \n
pueden representar valores con hasta 15 dígitos después del punto decimal1.\n Sin embargo, \n
los números flotantes no pueden representar exactamente algunos valores decimales, como 0.1 o 0.2\n
debido a que son fracciones binarias infinitas en base 22.Esto puede causar\n
 algunos errores de redondeo al realizar operaciones aritméticas con números flotantes.




"""


dato = input("Ingresa un numero entero ")

dato = int (dato) 

suma = (dato *(dato + 1)/2)
print(suma)

#TECNICATURA UNIVERSITARIA
#EN PROGRAMACIÓN
#A DISTANCIA

#Programación 1
#Práctico 6: Estructuras de datos complejas 

# Alunna Diaz Monroy Yohanna 

#Ejercicios :

# 1) Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Añadir las siguientes frutas con sus respectivos precios
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print("Diccionario después de añadir nuevas frutas:")
print(precios_frutas)

# 2) Actualizar los precios de las siguientes frutas
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print("\nDiccionario después de actualizar los precios:")
print(precios_frutas)

print ("##################")

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios.
lista_frutas = {'Banana','Ananá', 'Melón', 'Uva','Naranja', 'Manzana', 'Pera'}
print(lista_frutas)

print ("###################")

#4) Escribí un programa que permita almacenar y consultar números telefónicos.
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#• Luego, pedí un nombre y mostrale el número asociado, si existe.

# Crear diccionario vacío para los contactos
agenda = {}

# Pedir al usuario que ingrese 5 contactos
for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto {i+1}: ")
    numero = input(f"Ingresá el número de {nombre}: ")
    agenda[nombre] = numero  # Guardar en el diccionario

# Consultar un número telefónico
consulta = input("Ingresá el nombre del contacto que querés buscar: ")

# Mostrar el número si existe
if consulta in agenda:
    print(f"El número de {consulta} es {agenda[consulta]}")
else:
    print(f"{consulta} no se encuentra en la agenda.")

#5) Solicita al usuario una frase e imprime:
#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingresá una frase: ")
mi_set = {frase}

print(mi_set)

print ("############################")

#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.

# Crear un diccionario para almacenar los alumnos y sus notas
alumnos = {}

# Pedir al usuario los nombres y notas de 3 alumnos
for _ in range(3):
    nombre = input("Ingresá el nombre del alumno: ")
    notas = tuple(map(float, input("Ingresá las 3 notas separadas por espacio: ").split()))
    alumnos[nombre] = notas  # Guardar en el diccionario

# Calcular y mostrar el promedio de cada alumno
print("\nPromedios de cada alumno:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")

Print ("#########################")

#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
#y Parcial 2:
#• Mostrá los que aprobaron ambos parciales.
#• Mostrá los que aprobaron solo uno de los dos.
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir)

aprobados_parcial_1 = {31,32,33,34,35,36,37,38}
aprobados_parcial_2 = {39,40,41,42,43,44,45,46}

aprobados_ambos = aprobados_parcial_1 & aprobados_parcial_2

aprobados_solo_uno = aprobados_parcial_1 ^ aprobados_parcial_2

aprobados_total = aprobados_parcial_1 | aprobados_parcial_2

print("Estudiantes que aprobaron ambos parciales:", aprobados_ambos)
print("Estudiantes que aprobaron solo uno de los dos:", aprobados_solo_uno)
print("Lista total de estudiantes que aprobaron al menos un parcial:", aprobados_total)

print ("######################################")


#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
#Permití al usuario:
#• Consultar el stock de un producto ingresado.
#• Agregar unidades al stock si el producto ya existe.
#• Agregar un nuevo producto si no existe

Productos = ['queso': 1200, 'harina': 2500, 'azucar': 3000, 'te': 1450'huevos': 1200, 'cafe': 2500, 'fideos': 3000, 'avena': 1450 ]

print(Productos)
print(type(Productos))



print ("###########################################")

#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.

agenda = {}

agenda[("Lunes", "10:00")] = "clase de zoom "
agenda[("Martes", "14:30")] = "visitar a la abuela "
agenda[("Miércoles", "18:00")] = "llevar a perro al veterinario"
agenda[("Jueves", "09:00")] = "desayuno con mi mamá"
agenda[("Viernes", "20:00")] = "Cena con amigas"

print("\nAgenda semanal:")
for (dia, hora), evento in agenda.items():
    print(f"{dia} a las {hora}: {evento}")




print ("###########################################")

#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
#diccionario donde:
#• Las capitales sean las claves.
#• Los países sean los valores.


paises_capitales = {
    "Argentina": "Buenos Aires",
    "Ecuador": "Quito",
    "Bolivia": "La_Paz",
    "Espania": "Madrid",
    "Corea": "Seul"
}

# Invertir el diccionario: capitales como claves y países como valores
capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}

# Mostrar el nuevo diccionario
print(capitales_paises)
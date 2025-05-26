# TP numero 7 Programacion I Diaz Monroy Yohanna

# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario


def factorial_recursivo(n):
  if n < 0:
    return None
  elif n == 0:
    return 1
  else:
    return n * factorial_recursivo(n - 1)

if __name__ == "__main__":
  try:
    num_usuario = int(input("Ingrese un número entero positivo: "))
    if num_usuario < 1:
      print("Por favor, ingrese un número entero positivo.")
    else:
      print(f"\nFactoriales desde 1 hasta {num_usuario}:")
      for i in range(1, num_usuario + 1):
        factorial = factorial_recursivo(i)
        print(f"El factorial de {i} es: {factorial}")
  except ValueError:
    print("Entrada inválida. Por favor, ingrese un número entero.")


print ("###################################")

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique.


def fibonacci_recursivo(n):

  if n < 0:
    return None
  elif n <= 1:
    return n
  else:
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

if __name__ == "__main__":
  try:
    posicion_usuario = int(input("Ingrese la posición hasta la cual desea ver la serie de Fibonacci: "))
    if posicion_usuario < 0:
      print("Por favor, ingrese un número entero no negativo.")
    else:
      print(f"\nSerie de Fibonacci hasta la posición {posicion_usuario}:")
      for i in range(posicion_usuario + 1):
        valor_fib = fibonacci_recursivo(i)
        print(f"Fibonacci({i}) = {valor_fib}")
  except ValueError:
    print("Entrada inválida. Por favor, ingrese un número entero.")


print ("###################################")




#3) Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula n 𝑚 = 𝑛 ∗ 𝑛 (𝑚−1)
# . Prueba esta función en un algoritmo general.


def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

# Prueba de la función
base = 2
exponente = 4
resultado = potencia(base, exponente)
print(f"{base}^{exponente} = {resultado}")



print ("###################################")



#4) Crear una función recursiva en Python que reciba un número entero positivo en base
# decimal y devuelva su representación en binario como una cadena de texto.
# Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y
# unos (1), en base 2. Para convertir un número decimal a binario, se puede seguir este
# procedimiento:
# 1. Dividir el número por 2.
# 2. Guardar el resto (0 o 1).
# 3. Repetir el proceso con el cociente hasta que llegue a 0.
# 4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.


# Convertir el número 10 a binario:
# 10 ÷ 2 = 5 resto: 0
# 5 ÷ 2 = 2 resto: 1
# 2 ÷ 2 = 1 resto: 0
# 1 ÷ 2 = 0 resto: 1
# Leyendo los restos de abajo hacia arriba: 1 0 1 0 → El resultado binario es "1010".


def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

# Prueba de la función
numero = 10
resultado = decimal_a_binario(numero)
print(f"El número {numero} en binario es: {resultado}")


print ("###################################")


#5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
# Requisitos:
# La solución debe ser recursiva. No se debe usar [::-1] ni la función reversed().


def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

# Prueba de la función
palabra = "precocer"
print(f"¿'{palabra}' es un palíndromo? {es_palindromo(palabra)}")

palabra = "peces "
print(f"¿'{palabra}' es un palíndromo? {es_palindromo(palabra)}")


print ("###################################")


# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.
# Restricciones:
#No se puede convertir el número a string.
#Usá operaciones matemáticas (%, //) y recursión.
#Ejemplos:
#suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
#suma_digitos(9) → 9
#suma_digitos(305) → 8 (3 + 0 + 5)


def suma_digitos(n):
    if n == 0:
        return 0
    return (n % 10) + suma_digitos(n // 10)

# Prueba de la función
print(suma_digitos(1234))  # Devuelve 10
print(suma_digitos(9))     # Devuelve 9
print(suma_digitos(305))   # Devuelve 8


print ("###################################")


#7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
#bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
#último nivel con un solo bloque.
#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
#nivel más bajo y devuelva el total de bloques que necesita para construir toda la
#pirámide.
# Ejemplos:
#contar_bloques(1) → 1 (1)
#contar_bloques(2) → 3 (2 + 1)
#contar_bloques(4) → 10 (4 + 3 + 2 + 1)

defef contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

# Prueba de  función
print(contar_bloques(1))  # Devuelve 1
print(contar_bloques(2))  # Devuelve 3 (2 + 1)
print(contar_bloques(4))  # Devuelve 10 (4 + 3 + 2 + 1)


print ("###################################")



#8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
#número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
#aparece ese dígito dentro del número.
# Ejemplos:
#contar_digito(12233421, 2) → 3
#contar_digito(5555, 5) → 4 
#contar_digito(123456, 7) → 0 

def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

# Prueba de la función
print(contar_bloques(1))  # Devuelve 1
print(contar_bloques(2))  # Devuelve 3 (2 + 1)
print(contar_bloques(4))  # Devuelve 10 (4 + 3 + 2 + 1)


print ("###################################")
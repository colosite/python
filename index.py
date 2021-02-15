# Acá va un comentario
if 3 > 5:
    print("Esto no se va a imprimir, porque 3 no es mayor que 5")

# if 5 > 3: # Acá va otro comentario
    # print("5 es mayor a 3")


x = 5
y = "chanchito feliz"

print(x, y)

correo = "chanchito@feliz.com"

print(correo)

mi_variable = "Soy Luciano"
a, b, c = "lala", "lele", "lili"

# print(a, b, c)

valor1 = valor2 = valor3 = "texto repetido"

# print(valor1, valor2, valor3)

inicio = "Hello "
final = "world!"

print(inicio + final)

palabra = "numeros:" # string

entero = 20 # integer
conDecimales = 20.2 # float
complejo = 1j

print(palabra, entero, conDecimales, complejo)

lista = ["Lechuga", "Tomate", "Pan frances"]

lista.remove("Lechuga")
lista.remove("Tomate")
print(lista)

rango = range(6)
# print(rango)

diccionario = {
    "lenguaje": "python",
    "edad": 30
}

print(diccionario.get("lenguaje"))

gata = dict(nombre="Cata", edad=1)
print(gata)

verdadero = True # booleano 
falso = False # booleano

print(verdadero, falso)
# Cadenas, listas, tuplas y diccionarios
texto = 'Cadena de prueba'
texto2 = ' mensaje 2.'

print(texto + ' ' + texto2)
print(texto[3])
print(len(texto))

# lista
lista = ['manzanas', 'platanos', 'uvas', 1, 35, ['a', 'b', 'c']]
lista.append('hola')
print(lista)
print(lista[5][0])

lista.insert(0, 'hola man')
print(lista)
lista.remove('uvas')
print(lista)

## Diccionario 
diccionario = {'nombre': 'Juan', 'edad': 47}

print(diccionario['nombre'])
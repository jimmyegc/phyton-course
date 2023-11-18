# funciones
# def simples
def saludar(mensaje):
  print('Hola ', mensaje)

def saludar2(mensaje = 'Hola mundo!'):
  print(mensaje)

def saludar3(*lista):
  print(lista)

def saludar4(*diccionario):
  print(diccionario)  

saludar('¿Qué hace?')
saludar2()
saludar3(['uno', 'dos', 'tres'])
dict = {'nombre': 'Juan', 'edad': 47}
saludar4(dict)
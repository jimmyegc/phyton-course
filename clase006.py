# Clases
class Persona():
  nombre = ''
  apellidos = ''
  edad = 0

  def __init__(self):
    self.edad = 18

  def full_name(self):
    return self.nombre + '-' + self.apellidos
  
persona = Persona()
print(persona.edad)
print(persona.full_name())
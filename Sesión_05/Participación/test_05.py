"""
    Programación Orientada a Objetos
    Participación

Requerimientos:
    - Crear una Clase Alumno
    - Debe tener un atributo de nacionalidad con el valor "Peruano"
    - Tendrá 3 notas, la nota inicial de c/u será de 0
    - Crear un método que indicará el promedio del alumno
    - Crear un método que indicará si el alumno está aprobado o no de acuerdo a su promedio
    - Las notas serán pasadas por parámetro al momento de instanciar la clase
    - Crear un método para obtener el nombre y distrito de residencia del alumno
    - Instanciar la clase para el caso de 2 alumnos necesariamente
"""

#Creacion de clase
class Alumno:
    nacionalidad = "Peruano"
    def __init__(self, nombre, distrito, nota1=0, nota2=0, nota3=0):
        self.nombre = nombre
        self.distrito = distrito
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def promedio(self):
        promedio = (self.nota1 + self.nota2 + self.nota3) / 3
        return promedio

    def esta_aprobado(self):
        promedio = self.promedio()
        if promedio >= 10.5:
           return print(f"{self.nombre} esta aprobado/a y su promedio es {promedio:.2f}")
        else:
           return print(f"{self.nombre} tiene de promedio: {promedio:.2f}, esta desaprobado/a")

    def residencia(self):
        return f"Nombre alumno: {self.nombre}, Distrito: {self.distrito}"


#Instanciar alumnos
alumno_1 = Alumno("Maria", "Lince", 12, 18, 14)
alumno_2 = Alumno("Francisco", "Lince", 13, 10, 5)


#Mostrar datos
print(alumno_1.residencia())
print(f"Nacionalidad: {alumno_1.nacionalidad}")
print(f"Promedio: {alumno_1.promedio():.2f}")
alumno_1.esta_aprobado()

print(" ")

print(alumno_2.residencia())
print(f"Nacionalidad: {alumno_2.nacionalidad}")
print(f"Promedio: {alumno_2.promedio():.2f}")
alumno_2.esta_aprobado()


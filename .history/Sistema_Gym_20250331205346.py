from abc import ABC, abstractmethod
from Pool_Conexion import Conexion
from datetime import date

# Clase abstracta Persona
class Persona(ABC):
    def __init__(self, nombre, apellido, telefono, correo):
        self._nombre = nombre
        self._apellido = apellido
        self._telefono = telefono
        self._correo = correo

    @abstractmethod
    def guardar(self):
        pass
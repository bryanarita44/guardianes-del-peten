from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, codigo, nombre, en_peligro):
        self.codigo = codigo          # Artículo 1: formato AAA-000
        self.nombre = nombre
        self.en_peligro = en_peligro  # Artículo 2: True o False
        self.collar = None            # Artículo 4: un animal lleva un solo collar a la vez

    def tiene_collar(self):
        # Lo usan todas las especies tal cual
        return self.collar is not None

    def descripcion(self):
        # Datos que comparten todos los animales
        return f"{self.codigo} - {self.nombre} ({type(self).__name__})"

    @abstractmethod
    def describir(self):
        # Nadie es "animal a secas": cada especie lo implementa a su manera
        pass

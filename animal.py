class Animal:
    def __init__(self, codigo, nombre, especie, en_peligro):
        self.codigo = codigo          # Artículo 1: formato AAA-000
        self.nombre = nombre
        self.especie = especie
        self.en_peligro = en_peligro  # Artículo 2: True o False
        self.collar = None            # Artículo 4: un animal lleva un solo collar a la vez

    def tiene_collar(self):
        # Lo usan todas las especies tal cual
        return self.collar is not None

    def descripcion(self):
        # Datos que comparten todos los animales
        return f"{self.codigo} - {self.nombre} ({self.especie})"

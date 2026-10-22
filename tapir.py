from animal import Animal


class Tapir(Animal):
    def __init__(self, codigo, nombre, peso_kg=200):
        super().__init__(codigo, nombre, "tapir", True)
        self.peso_kg = peso_kg  # atributo propio del tapir

    def descripcion(self):
        # Sobrescribe el método del padre y lo reutiliza con super()
        return super().descripcion() + f" | peso: {self.peso_kg} kg"

    def es_adulto(self):
        # Método propio del tapir
        return self.peso_kg >= 150

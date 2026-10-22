from animal import Animal


class Jaguar(Animal):
    def __init__(self, codigo, nombre, territorio_km2=50):
        super().__init__(codigo, nombre, "jaguar", True)
        self.territorio_km2 = territorio_km2  # atributo propio del jaguar

    def descripcion(self):
        # Sobrescribe el método del padre y lo reutiliza con super()
        return super().descripcion() + f" | territorio: {self.territorio_km2} km2"

    def tipo_de_territorio(self):
        # Método propio del jaguar
        if self.territorio_km2 >= 50:
            return "grande"
        return "pequeño"

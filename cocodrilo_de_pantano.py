from animal import Animal


class CocodriloDePantano(Animal):
    def __init__(self, codigo, nombre, largo_m=3):
        super().__init__(codigo, nombre, "cocodrilo de pantano", False)
        self.largo_m = largo_m  # atributo propio del cocodrilo

    def descripcion(self):
        # Sobrescribe el método del padre y lo reutiliza con super()
        return super().descripcion() + f" | largo: {self.largo_m} m"

    def riesgo_para_personas(self):
        # Método propio del cocodrilo
        if self.largo_m >= 3:
            return "alto"
        return "bajo"

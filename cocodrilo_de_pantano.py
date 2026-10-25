from animal import Animal


class CocodriloDePantano(Animal):
    def __init__(self, codigo, nombre, largo_m=3):
        super().__init__(codigo, nombre, False)
        self.largo_m = largo_m  # atributo propio del cocodrilo

    def descripcion(self):
        # Sobrescribe el método del padre y lo reutiliza con super()
        return super().descripcion() + f" | largo: {self.largo_m} m"

    def riesgo_para_personas(self):
        # Método propio del cocodrilo
        if self.largo_m >= 3:
            return "alto"
        return "bajo"

    def describir(self):
        return (f"{self.nombre} es un cocodrilo de pantano de {self.largo_m} m de largo. "
                "Come peces, aves y mamíferos pequeños. "
                "Vive en lagunas, pantanos y ríos de corriente lenta. "
                "Se mueve nadando y camina con el cuerpo cerca del suelo.")

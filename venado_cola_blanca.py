from animal import Animal


class VenadoColaBlanca(Animal):
    def __init__(self, codigo, nombre, num_puntas=8):
        super().__init__(codigo, nombre, False)
        self.num_puntas = num_puntas  # atributo propio del venado

    def descripcion(self):
        # Sobrescribe el método del padre y lo reutiliza con super()
        return super().descripcion() + f" | puntas: {self.num_puntas}"

    def es_macho(self):
        # Método propio del venado (las hembras no tienen cuernos)
        return self.num_puntas > 0

    def describir(self):
        return (f"{self.nombre} es un venado cola blanca con {self.num_puntas} puntas. "
                "Come hierbas, hojas y frutos. "
                "Vive en bosques y matorrales. "
                "Camina con cuidado, y si se asusta corre, salta y levanta la cola blanca.")

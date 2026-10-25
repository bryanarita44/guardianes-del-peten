from animal import Animal


class GuacamayaRoja(Animal):
    def __init__(self, codigo, nombre, envergadura_cm=100):
        super().__init__(codigo, nombre, True)
        self.envergadura_cm = envergadura_cm  # atributo propio de la guacamaya

    def descripcion(self):
        # Sobrescribe el método del padre y lo reutiliza con super()
        return super().descripcion() + f" | envergadura: {self.envergadura_cm} cm"

    def puede_volar_lejos(self):
        # Método propio de la guacamaya
        return self.envergadura_cm >= 90

    def describir(self):
        return (f"{self.nombre} es una guacamaya roja de {self.envergadura_cm} cm de ala a ala. "
                "Come semillas, frutos y nueces. "
                "Vive en las copas de los árboles altos y anida en sus huecos. "
                "Se mueve volando, en pareja o en grupo.")

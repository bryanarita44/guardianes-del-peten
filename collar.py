class Collar:
    def __init__(self, codigo, bateria):
        self.codigo = codigo      # Artículo 10: no se repite entre collares
        self.bateria = bateria    # Artículo 3: nivel de 0 a 100
        self.animal = None        # Artículo 4: un collar se asigna a un solo animal
        self.cambios_bateria = [] # Artículo 9: quién cambió la batería y a qué nivel

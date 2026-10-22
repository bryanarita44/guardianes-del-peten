class Lectura:
    def __init__(self, animal, zona, hora, tipo, guardarrecursos=None):
        self.animal = animal
        self.zona = zona
        self.hora = hora
        self.tipo = tipo                      # "reporte" (del collar) o "avistamiento"
        self.guardarrecursos = guardarrecursos  # código de quien lo vio (solo avistamientos)

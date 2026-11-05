class Alerta:
    def __init__(self, numero, tipo, prioridad, detalle, hora):
        self.numero = numero
        self.tipo = tipo
        self.prioridad = prioridad
        self.detalle = detalle
        self.hora = hora           # Entrega 4: formato HH:MM, sirve para desempatar al ordenar
        self.estado = "pendiente"  # Artículo 8: toda alerta nace pendiente
        self.atendida_por = None   # Artículo 8: código de quien la atendió

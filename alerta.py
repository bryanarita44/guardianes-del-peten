class Alerta:
    def __init__(self, numero, tipo, prioridad, detalle):
        self.numero = numero
        self.tipo = tipo
        self.prioridad = prioridad
        self.detalle = detalle
        self.estado = "pendiente"  # Artículo 8: toda alerta nace pendiente
        self.atendida_por = None   # Artículo 8: código de quien la atendió

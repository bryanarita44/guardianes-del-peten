class ServicioSMS:
    # Simula el servicio externo de mensajes de texto que contrató la oficina
    def __init__(self):
        self.mensajes_enviados = []

    def enviar(self, guardarrecursos, mensaje):
        self.mensajes_enviados.append(mensaje)
        print(f"SMS enviado a {guardarrecursos.nombre} ({guardarrecursos.codigo}): {mensaje}")

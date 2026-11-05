from jaguar import Jaguar
from tapir import Tapir
from guacamaya_roja import GuacamayaRoja
from cocodrilo_de_pantano import CocodriloDePantano
from venado_cola_blanca import VenadoColaBlanca
from collar import Collar
from zona import Zona
from lectura import Lectura
from alerta import Alerta
from guardarrecursos import Guardarrecursos
from servicio_sms import ServicioSMS


def nivel(alerta):
    # Entrega 4: convierte la prioridad (texto) en un número para poder compararla
    if alerta.prioridad == "alta":
        return 1
    return 2


class SistemaMonitoreo:
    # Artículo 2: especies conocidas y si están en peligro (venado cola blanca es la especie agregada)
    ESPECIES = {
        "jaguar": True,
        "tapir": True,
        "guacamaya roja": True,
        "cocodrilo de pantano": False,
        "venado cola blanca": False,
    }

    # Entrega 2: la clase hija que corresponde a cada especie
    CLASES = {
        "jaguar": Jaguar,
        "tapir": Tapir,
        "guacamaya roja": GuacamayaRoja,
        "cocodrilo de pantano": CocodriloDePantano,
        "venado cola blanca": VenadoColaBlanca,
    }

    # Artículo 5: los únicos tipos de zona permitidos
    TIPOS_ZONA = ("núcleo", "amortiguamiento", "uso múltiple")

    def __init__(self):
        # Los arreglos de objetos del sistema
        self.animales = []
        self.collares = []
        self.zonas = []
        self.lecturas = []
        self.alertas = []
        self.guardarrecursos = []
        self.guardarrecursos_de_turno = None
        self.servicio_sms = ServicioSMS()

    # ------------------------------------------------------------------
    # Búsquedas: recorren las listas
    # ------------------------------------------------------------------
    def buscar_animal(self, codigo):
        # Entrega 4: búsqueda binaria. Primero se ordena la lista por código (selección)
        total = len(self.animales)
        for i in range(total - 1):
            menor = i
            for j in range(i + 1, total):
                if self.animales[j].codigo < self.animales[menor].codigo:
                    menor = j
            if menor != i:
                temporal = self.animales[i]
                self.animales[i] = self.animales[menor]
                self.animales[menor] = temporal
        # Ahora se parte la lista a la mitad hasta encontrar el código
        inicio = 0
        fin = len(self.animales) - 1
        while inicio <= fin:
            medio = (inicio + fin) // 2
            animal = self.animales[medio]
            if animal.codigo == codigo:
                return animal
            if codigo < animal.codigo:
                fin = medio - 1
            else:
                inicio = medio + 1
        return None

    def buscar_collar(self, codigo):
        for collar in self.collares:
            if collar.codigo == codigo:
                return collar
        return None

    def buscar_zona(self, nombre):
        for zona in self.zonas:
            if zona.nombre == nombre:
                return zona
        return None

    def buscar_guardarrecursos(self, codigo):
        for guardarrecurso in self.guardarrecursos:
            if guardarrecurso.codigo == codigo:
                return guardarrecurso
        return None

    def buscar_alerta(self, numero):
        for alerta in self.alertas:
            if alerta.numero == numero:
                return alerta
        return None

    # ------------------------------------------------------------------
    # Validaciones de formato (reutilizadas por las guardas)
    # ------------------------------------------------------------------
    def codigo_animal_valido(self, codigo):
        # Artículo 1: 3 letras mayúsculas, un guion y 3 dígitos (ej. JAG-001)
        return (isinstance(codigo, str)
                and len(codigo) == 7
                and codigo[:3].isalpha() and codigo[:3].isupper()
                and codigo[3] == "-"
                and codigo[4:].isdigit())

    def codigo_guardarrecursos_valido(self, codigo):
        # Artículo 7: 2 letras mayúsculas, un guion y 2 dígitos (ej. GR-07)
        return (isinstance(codigo, str)
                and len(codigo) == 5
                and codigo[:2].isalpha() and codigo[:2].isupper()
                and codigo[2] == "-"
                and codigo[3:].isdigit())

    def nivel_bateria_valido(self, nivel):
        # Artículo 3: el nivel de batería va de 0 a 100
        return isinstance(nivel, int) and 0 <= nivel <= 100

    # ------------------------------------------------------------------
    # Registros básicos
    # ------------------------------------------------------------------
    def registrar_zona(self, nombre, tipo):
        # Artículo 5: solo existen tres tipos de zona
        if tipo not in self.TIPOS_ZONA:
            print(f"Zona rechazada: el tipo '{tipo}' no existe (núcleo, amortiguamiento o uso múltiple)")
            return None
        zona = Zona(nombre, tipo)
        self.zonas.append(zona)
        print(f"Zona registrada: {nombre} ({tipo})")
        return zona

    def registrar_guardarrecursos(self, codigo, nombre):
        # Artículo 7: sin un código válido no se registra nada a su nombre
        if not self.codigo_guardarrecursos_valido(codigo):
            print(f"Guardarrecursos rechazado: el código '{codigo}' debe ser como GR-07")
            return None
        guardarrecurso = Guardarrecursos(codigo, nombre)
        self.guardarrecursos.append(guardarrecurso)
        print(f"Guardarrecursos registrado: {codigo} - {nombre}")
        return guardarrecurso

    def definir_turno(self, codigo):
        guardarrecurso = self.buscar_guardarrecursos(codigo)
        if guardarrecurso is None:
            print(f"Turno rechazado: el guardarrecursos {codigo} no está registrado")
            return False
        self.guardarrecursos_de_turno = guardarrecurso
        print(f"De turno: {guardarrecurso.nombre} ({codigo})")
        return True

    def registrar_collar(self, codigo, bateria):
        # Artículo 10 (propio): no pueden existir dos collares con el mismo código
        if self.buscar_collar(codigo) is not None:
            print(f"Código de collar repetido rechazado: ya existe el collar {codigo}")
            return None
        # Artículo 3: el nivel de batería va de 0 a 100
        if not self.nivel_bateria_valido(bateria):
            print(f"Collar rechazado: la batería {bateria} debe estar entre 0 y 100")
            return None
        collar = Collar(codigo, bateria)
        self.collares.append(collar)
        print(f"Collar registrado: {codigo} con {bateria} % de batería")
        return collar

    def crear_alerta(self, tipo, prioridad, detalle, hora):
        alerta = Alerta(len(self.alertas) + 1, tipo, prioridad, detalle, hora)
        self.alertas.append(alerta)
        print(f"Alerta #{alerta.numero} creada ({tipo}, prioridad {prioridad}, {hora}): {detalle}")
        return alerta

    def ordenar_alertas(self):
        # Entrega 4: ordenamiento por selección. Primero las altas, y entre iguales la hora más temprana
        total = len(self.alertas)
        for i in range(total - 1):
            menor = i
            for j in range(i + 1, total):
                actual = self.alertas[j]
                mejor = self.alertas[menor]
                if nivel(actual) < nivel(mejor):
                    menor = j
                elif nivel(actual) == nivel(mejor) and actual.hora < mejor.hora:
                    menor = j
            if menor != i:
                temporal = self.alertas[i]
                self.alertas[i] = self.alertas[menor]
                self.alertas[menor] = temporal

    # ------------------------------------------------------------------
    # Casos de uso (siguen los diagramas de los anexos)
    # ------------------------------------------------------------------
    def registrar_animal(self, codigo, nombre, especie, en_peligro, dato_propio=None):
        # Anexo A. Artículo 1: formato correcto
        if not self.codigo_animal_valido(codigo):
            print(f"Código inválido rechazado: '{codigo}' debe ser como JAG-001")
            return None
        # Artículo 1: no pueden existir dos animales con el mismo código
        if self.buscar_animal(codigo) is not None:
            print(f"Código repetido rechazado: ya existe el animal {codigo}")
            return None
        # Artículo 2: la especie debe ser conocida
        if especie.lower() not in self.ESPECIES:
            print(f"Especie rechazada: '{especie}' no está en la lista de especies")
            return None
        # Artículo 2: el estado de peligro debe coincidir con la especie
        if self.ESPECIES[especie.lower()] != en_peligro:
            print(f"Estado rechazado: el estado de peligro no coincide con la especie {especie}")
            return None
        # Entrega 2: se crea la clase hija de la especie (dato_propio es opcional)
        clase = self.CLASES[especie.lower()]
        if dato_propio is None:
            animal = clase(codigo, nombre)
        else:
            animal = clase(codigo, nombre, dato_propio)
        self.animales.append(animal)
        print(f"Animal registrado: {codigo} - {nombre} ({especie})")
        return animal

    def asignar_collar(self, codigo_collar, codigo_animal):
        # Anexo B
        collar = self.buscar_collar(codigo_collar)
        animal = self.buscar_animal(codigo_animal)
        if collar is None or animal is None:
            print("Asignación rechazada: el collar o el animal no existen")
            return False
        # Artículo 4: un collar, un animal
        if collar.animal is not None:
            print(f"Asignación rechazada: el collar {collar.codigo} ya está asignado a {collar.animal.codigo}")
            return False
        # Artículo 4: un animal lleva un solo collar a la vez
        if animal.collar is not None:
            print(f"Asignación rechazada: el animal {animal.codigo} ya lleva el collar {animal.collar.codigo}")
            return False
        collar.animal = animal
        animal.collar = collar
        print(f"Collar {collar.codigo} asignado a {animal.codigo}")
        return True

    def reportar_posicion(self, codigo_collar, nombre_zona, hora):
        # Anexo C
        collar = self.buscar_collar(codigo_collar)
        if collar is None:
            print(f"Lectura rechazada: el collar {codigo_collar} no existe")
            return None
        # Artículo 3: con menos de 10 % el collar no puede reportar
        if collar.bateria < 10:
            print(f"Lectura rechazada: el collar {collar.codigo} tiene {collar.bateria} % de batería (mínimo 10 %)")
            self.crear_alerta("batería baja", "media", f"Collar {collar.codigo} con {collar.bateria} % de batería", hora)
            return None
        # Artículo 5: solo se aceptan lecturas en zonas registradas
        zona = self.buscar_zona(nombre_zona)
        if zona is None:
            print(f"Lectura rechazada: la zona '{nombre_zona}' no está registrada")
            return None
        if collar.animal is None:
            print(f"Lectura rechazada: el collar {collar.codigo} no está asignado a ningún animal")
            return None
        lectura = Lectura(collar.animal, zona, hora, "reporte")
        self.lecturas.append(lectura)
        print(f"Lectura registrada: {collar.animal.codigo} en {zona.nombre} a las {hora}")
        # Artículo 6: animal en peligro en zona de uso múltiple
        if collar.animal.en_peligro and zona.tipo == "uso múltiple":
            detalle = f"{collar.animal.nombre} ({collar.animal.codigo}) en {zona.nombre}"
            alerta = self.crear_alerta("acercamiento a comunidad", "alta", detalle, hora)
            self.notificar_por_sms(alerta)
        return lectura

    def notificar_por_sms(self, alerta):
        # Artículo 6: la alerta se envía por el servicio de SMS al guardarrecursos de turno
        if self.guardarrecursos_de_turno is None:
            print("No hay guardarrecursos de turno: no se pudo enviar el SMS")
            return
        mensaje = f"Alerta #{alerta.numero} {alerta.prioridad}: {alerta.detalle}"
        self.servicio_sms.enviar(self.guardarrecursos_de_turno, mensaje)

    def registrar_avistamiento(self, codigo_guardarrecursos, codigo_animal, nombre_zona, hora):
        # Anexo D. Artículo 7: sin código válido no se registra nada
        if not self.codigo_guardarrecursos_valido(codigo_guardarrecursos):
            print(f"Avistamiento rechazado: el código '{codigo_guardarrecursos}' debe ser como GR-07")
            return None
        animal = self.buscar_animal(codigo_animal)
        zona = self.buscar_zona(nombre_zona)
        if animal is None or zona is None:
            print("Avistamiento rechazado: el animal o la zona no existen")
            return None
        lectura = Lectura(animal, zona, hora, "avistamiento", codigo_guardarrecursos)
        self.lecturas.append(lectura)
        print(f"Avistamiento registrado: {animal.codigo} en {zona.nombre} a las {hora} (visto por {codigo_guardarrecursos})")
        return lectura

    def listar_alertas_pendientes(self):
        pendientes = []
        for alerta in self.alertas:
            if alerta.estado == "pendiente":
                pendientes.append(alerta)
        print(f"Alertas pendientes: {len(pendientes)}")
        for alerta in pendientes:
            print(f"  #{alerta.numero} [{alerta.prioridad}] {alerta.tipo}: {alerta.detalle}")
        return pendientes

    def atender_alerta(self, numero, codigo_guardarrecursos):
        # Anexo E. Artículo 7: sin código válido no se registra nada a su nombre
        if not self.codigo_guardarrecursos_valido(codigo_guardarrecursos):
            print(f"Atención rechazada: el código '{codigo_guardarrecursos}' debe ser como GR-07")
            return False
        alerta = self.buscar_alerta(numero)
        if alerta is None:
            print(f"Atención rechazada: la alerta #{numero} no existe")
            return False
        # Artículo 8: una alerta se atiende una sola vez
        if alerta.estado == "atendida":
            print(f"Sin cambios: la alerta #{numero} ya fue atendida por {alerta.atendida_por}")
            return False
        alerta.estado = "atendida"
        alerta.atendida_por = codigo_guardarrecursos
        print(f"Alerta #{numero} atendida por {codigo_guardarrecursos}")
        return True

    def registrar_cambio_bateria(self, codigo_guardarrecursos, codigo_collar, nuevo_nivel):
        # Caso de uso escondido. Artículo 9: lo registra un guardarrecursos con su código
        if not self.codigo_guardarrecursos_valido(codigo_guardarrecursos):
            print(f"Cambio rechazado: el código '{codigo_guardarrecursos}' debe ser como GR-07")
            return False
        collar = self.buscar_collar(codigo_collar)
        if collar is None:
            print(f"Cambio rechazado: el collar {codigo_collar} no existe")
            return False
        # Artículo 9: el nuevo nivel cumple con el artículo 3 (0 a 100)
        if not self.nivel_bateria_valido(nuevo_nivel):
            print(f"Cambio rechazado: el nivel {nuevo_nivel} debe estar entre 0 y 100")
            return False
        collar.bateria = nuevo_nivel
        collar.cambios_bateria.append(f"{codigo_guardarrecursos}: {nuevo_nivel} %")
        print(f"Cambio de batería registrado por {codigo_guardarrecursos}: collar {collar.codigo} ahora con {nuevo_nivel} %")
        return True

    def consultar_movimientos(self, codigo_animal):
        # Anexo F
        animal = self.buscar_animal(codigo_animal)
        if animal is None:
            print(f"Consulta sin resultados: el animal {codigo_animal} no existe")
            return []
        movimientos = []
        for lectura in self.lecturas:
            if lectura.animal.codigo == codigo_animal:
                movimientos.append(lectura)
        print(f"Movimientos de {animal.nombre} ({animal.codigo}): {len(movimientos)}")
        for lectura in movimientos:
            print(f"  {lectura.hora} - {lectura.zona.nombre} ({lectura.tipo})")
        return movimientos

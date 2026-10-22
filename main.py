from sistema import SistemaMonitoreo

sistema = SistemaMonitoreo()

print("=== ZONAS (artículo 5) ===")
sistema.registrar_zona("Laguna del Tigre", "núcleo")
sistema.registrar_zona("Mirador-Río Azul", "núcleo")
sistema.registrar_zona("Amortiguamiento Norte", "amortiguamiento")
sistema.registrar_zona("Uaxactún", "uso múltiple")
sistema.registrar_zona("Zona Misteriosa", "turística")  # RECHAZO 1: tipo inexistente

print("\n=== GUARDARRECURSOS (artículo 7) ===")
sistema.registrar_guardarrecursos("GR-07", "Mateo Chayax")
sistema.registrar_guardarrecursos("gr07", "Código Malo")  # RECHAZO 2: código inválido
sistema.definir_turno("GR-07")

print("\n=== ANIMALES (artículos 1 y 2) ===")
sistema.registrar_animal("JAG-001", "Balam", "jaguar", True, 70)
sistema.registrar_animal("TAP-001", "Tziquin", "tapir", True, 220)
sistema.registrar_animal("GUA-001", "Kinich", "guacamaya roja", True)
sistema.registrar_animal("COC-001", "Chaac", "cocodrilo de pantano", False, 4)
sistema.registrar_animal("VEN-001", "Ceh", "venado cola blanca", False, 10)
sistema.registrar_animal("jag001", "Balam", "jaguar", True)   # RECHAZO 3: formato inválido
sistema.registrar_animal("JAG-001", "Otro", "jaguar", True)   # RECHAZO 4: código repetido
sistema.registrar_animal("TAP-002", "Falso", "tapir", False)  # RECHAZO 5: peligro no coincide

print("\n=== COLLARES (artículos 3 y 10) ===")
sistema.registrar_collar("COL-01", 80)
sistema.registrar_collar("COL-02", 8)
sistema.registrar_collar("COL-03", 55)
sistema.registrar_collar("COL-04", 60)   # queda libre para probar el artículo 4
sistema.registrar_collar("COL-01", 90)   # RECHAZO 6: código de collar repetido (artículo 10)
sistema.registrar_collar("COL-05", 150)  # RECHAZO 7: batería fuera de rango

print("\n=== ASIGNAR COLLAR (artículo 4) ===")
sistema.asignar_collar("COL-01", "JAG-001")
sistema.asignar_collar("COL-02", "TAP-001")
sistema.asignar_collar("COL-03", "VEN-001")
sistema.asignar_collar("COL-01", "GUA-001")  # RECHAZO 8: el collar ya está asignado
sistema.asignar_collar("COL-04", "JAG-001")  # RECHAZO 9: el animal ya lleva otro collar
sistema.asignar_collar("COL-99", "JAG-001")  # RECHAZO 10: el collar no existe

print("\n=== REPORTAR POSICIÓN (artículos 3, 5 y 6) ===")
sistema.reportar_posicion("COL-01", "Laguna del Tigre", "06:30")
sistema.reportar_posicion("COL-01", "Uaxactún", "18:30")       # animal en peligro: alerta alta y SMS
sistema.reportar_posicion("COL-03", "Uaxactún", "19:00")       # no está en peligro: sin alerta
sistema.reportar_posicion("COL-02", "Mirador-Río Azul", "07:00")  # RECHAZO 11: batería baja
sistema.reportar_posicion("COL-01", "Río Desconocido", "20:00")   # RECHAZO 12: zona no registrada

print("\n=== REGISTRAR AVISTAMIENTO (artículo 7) ===")
sistema.registrar_avistamiento("GR-07", "COC-001", "Laguna del Tigre", "09:15")
sistema.registrar_avistamiento("GR7", "COC-001", "Laguna del Tigre", "09:20")  # RECHAZO 13: código inválido

print("\n=== ATENDER ALERTA (artículo 8) ===")
sistema.listar_alertas_pendientes()
sistema.atender_alerta(1, "GR-07")
sistema.atender_alerta(1, "GR-07")  # RECHAZO 14: ya fue atendida
sistema.listar_alertas_pendientes()

print("\n=== CAMBIO DE BATERÍA (artículo 9) ===")
sistema.registrar_cambio_bateria("GR-07", "COL-02", 90)
sistema.registrar_cambio_bateria("GR-07", "COL-02", 120)  # RECHAZO 15: nivel fuera de rango
sistema.reportar_posicion("COL-02", "Mirador-Río Azul", "08:00")  # ahora sí puede reportar

print("\n=== CONSULTAR MOVIMIENTOS ===")
sistema.consultar_movimientos("JAG-001")
sistema.consultar_movimientos("TAP-001")
sistema.consultar_movimientos("XXX-000")  # el animal no existe

print("\n=== HERENCIA (Entrega 2) ===")
# Para cada especie: un método heredado sin cambios, uno sobrescrito y uno propio
jaguar = sistema.buscar_animal("JAG-001")
print("Jaguar    | heredado  tiene_collar():", jaguar.tiene_collar())
print("Jaguar    | sobrescrito descripcion():", jaguar.descripcion())
print("Jaguar    | propio    tipo_de_territorio():", jaguar.tipo_de_territorio())

tapir = sistema.buscar_animal("TAP-001")
print("Tapir     | heredado  tiene_collar():", tapir.tiene_collar())
print("Tapir     | sobrescrito descripcion():", tapir.descripcion())
print("Tapir     | propio    es_adulto():", tapir.es_adulto())

guacamaya = sistema.buscar_animal("GUA-001")
print("Guacamaya | heredado  tiene_collar():", guacamaya.tiene_collar())
print("Guacamaya | sobrescrito descripcion():", guacamaya.descripcion())
print("Guacamaya | propio    puede_volar_lejos():", guacamaya.puede_volar_lejos())

cocodrilo = sistema.buscar_animal("COC-001")
print("Cocodrilo | heredado  tiene_collar():", cocodrilo.tiene_collar())
print("Cocodrilo | sobrescrito descripcion():", cocodrilo.descripcion())
print("Cocodrilo | propio    riesgo_para_personas():", cocodrilo.riesgo_para_personas())

venado = sistema.buscar_animal("VEN-001")
print("Venado    | heredado  tiene_collar():", venado.tiene_collar())
print("Venado    | sobrescrito descripcion():", venado.descripcion())
print("Venado    | propio    es_macho():", venado.es_macho())

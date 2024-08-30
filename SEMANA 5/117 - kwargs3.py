def describir_persona(nombre,**kwargs):
    print(f"características de {nombre}:")
    for clave,valor in kwargs.items():
        print(f"{clave} - {valor}")

print(describir_persona("Juan",ojos="azules", cabello="marron",edad=15))
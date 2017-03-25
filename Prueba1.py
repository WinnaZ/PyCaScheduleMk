class Taller(object):
    def __init__(self, nombre, representante, categoria, dificultad):
        self.nombre = nombre
        self.representante = representante
        self.categoria = categoria
        self.dificultad = dificultad
    

def crear_taller():
    nombre_taller = str(input("Ingrese el nombre del taller: "))
    nombre_representante = str(input("Ingrese el nombre del representante: "))
    categoria = str(input("Ingrese la categoria: "))
    dificultad = int(input("Ingrese numero de dificultad: "))
    return Taller(nombre_taller, nombre_representante, categoria, dificultad)

def agregar_talleres():
    lista_de_talleres = []
    while(True):
        desicion = str(input("Desea ingresar un nuevo taller? S/N ")).lower()
        if desicion == 's':
            lista_de_talleres.append(crear_taller())
        elif desicion == 'n' :
            return lista_de_talleres
        else:
            print("Error al tomar la desicion, intente otra vez.")

talleres = agregar_talleres()
for taller in talleres:
    print(taller.nombre)
    print(taller.representante)
    print(taller.categoria)
    print(taller.dificultad)
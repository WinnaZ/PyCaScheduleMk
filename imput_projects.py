# -*- coding: utf-8 -*-
import json
from pprint import pprint

# loads the data from an existing .json into a dictiorary
data = json.load(open('input_example.json'))

UserName = str(input("¿Cuál es tu nombre?  "))
ProjectName = str(input("Ingresá el Nombre del Proyecto a proponer  "))

data['projects'][ProjectName] = {}
ProjectDif = 13

while ProjectDif not in range(1, 11):
    ProjectDif = input("Ingresá el grado de dificultad del proyecto (1-10)   ")
    if ProjectDif.isnumeric():
        ProjectDif = int(ProjectDif)

data['projects'][ProjectName]['difficult_level'] = ProjectDif
RespCheck = input("Sos el responsable de este proyecto? Si/No  ")
RespCheck = RespCheck.lower()


while RespCheck != "si" and RespCheck != "no":

    print("Por favor responde con 'Si' o 'No'")
    RespCheck = input("Sos el/la responsable de este proyecto? Si/No  ")
    RespCheck = RespCheck.lower()

if RespCheck == "si":

    data['projects'][ProjectName]['responsables'] = [UserName, ]

elif RespCheck == "no":

    ProjectResp = input("Por favor ingresa el nombre del responsable  ")
    data['projects'][ProjectName]['responsables'] = ProjectResp

addresp = str(input("¿Hay otrx responsable del proyecto? Si/No  "))
addresp = addresp.lower()

while addresp != "si" and addresp != "no":

    print("Por favor responde con 'Si' o 'No'")
    addresp = str(input("¿Hay otrx responsable del proyecto? Si/No  "))
    addresp = addresp.lower()

while addresp == "si":

    RespAdic = str(input("Ingresá el nombre de la persona responsable  "))
    data['projects'][ProjectName]['responsables'].append(RespAdic)
    addresp = str(input("¿Hay otrx responsable del proyecto? Si/No  "))
    addresp = addresp.lower()

    while addresp != "si" and addresp != "no":

        print("Por favor responde con 'Si' o 'No'")
        addresp = str(input("¿Hay otrx responsable del proyecto? Si/No  "))
        addresp = addresp.lower()

print ("La información fue cargada correctamente")
print ("Gracias!")

with open('input_example.json', 'w') as f:
    json.dump(data, f, indent=2)
# -*- coding: utf-8 -*-
import json
from pprint import pprint

# loads the data from an existing .json into a dictiorary
data = json.load(open('input_example.json'))

user_name = str(input("¿Cuál es tu nombre?  "))
project_name = str(input("Ingresá el Nombre del Proyecto a proponer  "))

data['projects'][project_name] = {}
project_dif = 13

while project_dif not in range(1, 11):
    project_dif = input("Ingresá el grado de dificultad del proyecto (1-10)  ")
    if project_dif.isnumeric():
        project_dif = int(project_dif)

data['projects'][project_name]['difficult_level'] = project_dif
resp_check = input("Sos el responsable de este proyecto? Si/No  ")
resp_check = resp_check.lower()


while resp_check != "si" and resp_check != "no":

    print("Por favor responde con 'Si' o 'No'")
    resp_check = input("Sos el/la responsable de este proyecto? Si/No  ")
    resp_check = resp_check.lower()

if resp_check == "si":

    data['projects'][project_name]['responsables'] = [user_name, ]

elif resp_check == "no":

    project_resp = input("Por favor ingresa el nombre del responsable  ")
    data['projects'][project_name]['responsables'] = project_resp

add_resp = str(input("¿Hay otrx responsable del proyecto? Si/No  "))
add_resp = add_resp.lower()

while add_resp != "si" and add_resp != "no":

    print("Por favor responde con 'Si' o 'No'")
    add_resp = str(input("¿Hay otrx responsable del proyecto? Si/No  "))
    add_resp = add_resp.lower()

while add_resp == "si":

    RespAdic = str(input("Ingresá el nombre de la persona responsable  "))
    data['projects'][project_name]['responsables'].append(RespAdic)
    add_resp = str(input("¿Hay otrx responsable del proyecto? Si/No  "))
    add_resp = add_resp.lower()

    while add_resp != "si" and add_resp != "no":

        print("Por favor responde con 'Si' o 'No'")
        add_resp = str(input("¿Hay otrx responsable del proyecto? Si/No  "))
        add_resp = add_resp.lower()

print ("La información fue cargada correctamente")
print ("Gracias!")

with open('input_example.json', 'w') as f:
    json.dump(data, f, indent=2)
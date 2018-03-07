# -*- coding: utf-8 -*-
import json
from pprint import pprint

# loads the data from an existing .json into a dictiorary
data = json.load(open('input_example.json'))

#given a certain boolean question loops you in until your answer is valid
def checkYesNo(question):
    resp = input(question + "  ").lower()
    while resp != "si" and resp != "no":
        print("Por favor responde con 'Si' o 'No'  ")
        resp = input(question).lower()
    return resp

user_name = str(input("¿Cuál es tu nombre?  "))
project_name = str(input("Ingresá el Nombre del Proyecto a proponer  "))
#import pdb; pdb.set_trace()

data['projects'][project_name] = {}
resp_check = 0
while resp_check not in range(1, 11):
    resp_check = input("Ingresá el grado de dificultad del proyecto (1-10  ")
    if resp_check.isnumeric():
        resp_check = int(resp_check)

data['projects'][project_name]['difficult_level'] = resp_check

resp_check = checkYesNo("Sos el responsable de este proyecto? Si/No  ")
print (resp_check)

if resp_check == "si":
    
    data['projects'][project_name]['responsables'] = [user_name, ]

elif resp_check == "no":

    project_resp = input("Por favor ingresa el nombre del responsable  ")
    data['projects'][project_name]['responsables'] = project_resp

resp_check = checkYesNo("¿Hay otrx responsable del proyecto? Si/No")

while resp_check == "si":

    resp_check = str(input("Ingresá el nombre de la persona responsable  "))
    data['projects'][project_name]['responsables'].append(resp_check)
    
resp_check = checkYesNo("¿Hay otrx responsable del proyecto? Si/No")
 
print ("La información fue cargada correctamente")
print ("Gracias!")

with open('input_example.json', 'w') as f:
    json.dump(data, f, indent=2)
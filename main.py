# -*- coding: utf-8 -*-
from project import Project
def menu():
    print "1) para ingresar "
    print "2) para salir "



out = False
while not out:
    menu()
    option = raw_input("")
    if option == "2":
        break
    elif option == "1":
        name = raw_input("Ingrese el nombre del Project: ")
        team_leader = raw_input("Ingrese el id: ")
        #Project['team_leader']['leader_name'] = raw_input("Ingrese el nombre del responsable:
        #Project['team_leader']['leader_name'= raw_input("Ingrese el nombre del responsable: ")
        category = raw_input("Ingrese la categoría del categoria: ")
        tags = raw_input("Ingrese el nombre del tag: ")
        p = Project(name, team_leader, category, tags)

#import pdb; pdb.set_trace()


       #

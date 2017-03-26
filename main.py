# -*- coding: utf-8 -*-
from project import Project
from vote import voting

def menu_enter():
    print "1) para ingresar "
    print "2) para salir "

def menu_vote():
    print "l) para levantar la mano "
    print "p) para pasar "


projects = []
out = False
while not out:
    menu_enter()
    option = raw_input("")
    if option == "2":
        break
    elif option == "1":
        name = raw_input("Ingrese el nombre del Project: ")
        ide = raw_input("Ingrese el id: ")
        team_leader = raw_input("Ingrese el responsable: ")
        category = raw_input("Ingrese la categoría del categoria: ")
        tags = raw_input("Ingrese el nombre del tag: ")

        p = Project(name, ide, team_leader, category, tags)
        projects.append(p)
#import pdb; pdb.set_trace()
out = False
while not out:
    menu_vote()
    choice = raw_input("")
    d = voting(projects, choice)
    print d
    if option == "s":
        break

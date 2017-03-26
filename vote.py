# -*- coding: utf-8 -*-
#import pdb; pdb.set_trace()


def voting(list_projects, choice):
    print ("Reglas de votación: "
           "l) levanta la mano  "
           "p) pasa esta votación")
    print "Estamos votando el projecto: "
    result = 0
    for n in range(0, len(list_projects)):
        if choice == "l":
            output = True
            result += 1
        elif choice == "p":
            output = False
    return result


#import pdb; pdb.set_trace()

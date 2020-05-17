import nltk
from nltk.tree import Tree
from nltk.draw import TreeView
import os

from gramaticas import grammar2, grammar1


def splitCadena(word): 
    return [char for char in word]  

def gramaticaToArbol(cadena, gramatica):

    #Returns nltk.Tree.Tree format output
    a = []  

    parser = nltk.ChartParser(gramatica)

    for tree in parser.parse(cadena):
        a.append(tree)

    return(a[0]) 

#cadena = splitCadena('(a,(a,(a),(a,a)))')
#cadena = splitCadena('001e')
cadena = input("Ingrese cadena a validar: ")

cadena = splitCadena(cadena)

#Gives output as structured tree   
arbol = gramaticaToArbol(cadena, grammar2)

print(arbol)

#Gives tree diagrem in tkinter window
arbol.draw()

# Bug si hay parentesis en los simbolos de la gramatica
t = Tree.fromstring(str(arbol))

TreeView(t)._cframe.print_to_file('./res/output.ps')

# Convertir el output.ps a .png
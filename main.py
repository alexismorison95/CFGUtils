import nltk
from nltk.tree import Tree
from nltk.draw import TreeView
import os

from gramaticas import grammar2, grammar1


def splitCadena(word): 
    return [char for char in word]  

def gramaticaToArbol(cadena, gramatica):

    a = []  

    parser = nltk.ChartParser(gramatica)

    for tree in parser.parse(cadena):
        a.append(tree)

    return(a[0]) 

cadenaInput = input("Ingrese cadena a validar: ")

try:
    cadena = splitCadena(cadenaInput)

    arbol = gramaticaToArbol(cadena, grammar2)

    print(arbol)

    arbol.draw()

    # Bug si hay parentesis en los terminales de la gramatica
    t = Tree.fromstring(str(arbol))

    TreeView(t)._cframe.print_to_file('./res/output.ps')

    # Convertir el output.ps a .png

except IndexError as error:
    
    print('La gramatica no genera la cadena ' + cadenaInput)

except Exception as ex:

    print(ex)
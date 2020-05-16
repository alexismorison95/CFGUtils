import nltk
from nltk.tree import Tree
from nltk.draw import TreeView

from gramaticas import grammar1


def splitCadena(word): 
    return [char for char in word]  

def gramaticaToArbol(cadena, gramatica):

    #Returns nltk.Tree.Tree format output
    a = []  

    parser = nltk.ChartParser(gramatica)

    for tree in parser.parse(cadena):
        a.append(tree)

    return(a[0]) 

cadena = splitCadena('(a,(a,(a),(a,a)))')

#Gives output as structured tree   
arbol = gramaticaToArbol(cadena, grammar1)

print(arbol)

#Gives tree diagrem in tkinter window
arbol.draw()

t = Tree.fromstring(str(arbol))

TreeView(t)._cframe.print_to_file('./res/output.ps')

# Convertir el output.ps a .png
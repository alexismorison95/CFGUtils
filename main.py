import nltk
from nltk.tree import Tree
from nltk.draw import TreeView

from gramaticas import grammar1, grammar2, grammar3


def splitCadena(word):
    """
    Funcion split simple para cuando la gramatica posee variables y terminales formados por un solo simbolo.\n
    Ej:\n
    S -> '(' L ')' | 'a' \n
    L -> L ',' S | S
    """ 

    return [char for char in word]


def splitCadena2(word):
    """
    Funcion split para cuando la gramatica posee variables y terminales formados por varios simbolos. \n
    Es necesario escribir la cadena a validar separando por espacios los simbolos y los terminales.\n
    Ej:\n
    S -> F S | F \n
    F -> 'FUNCTION' 'id' '(' P ')' C 'END' \n
    etc.
    """  

    return word.split()   


def gramaticaToArbol(cadena, gramatica):

    a = []  

    parser = nltk.ChartParser(gramatica)

    for tree in parser.parse(cadena):
        a.append(tree)

    return(a[0]) 


def generarArbol(cadenaInput, gramatica, funcionSplit):

    cadena = funcionSplit(cadenaInput)

    arbol = gramaticaToArbol(cadena, gramatica)

    arbol.pretty_print()
    
    arbol.draw()

    # Bug si hay parentesis en los terminales de la gramatica
    t = Tree.fromstring(str(arbol))

    TreeView(t)._cframe.print_to_file('./res/output.ps')


def main():

    print("La gramatica seleccionada es:")
    print(grammar3[1])

    cadenaInput = input("Ingrese cadena a validar: ")

    try:
        generarArbol(cadenaInput, grammar3[0], splitCadena)

    except IndexError:

        print('La gramatica no genera la cadena ' + cadenaInput)

    except:

        try:
            generarArbol(cadenaInput, grammar3[0], splitCadena2)

        except IndexError:

            print('La gramatica no genera la cadena ' + cadenaInput)
        
        except Exception as ex:

            print(ex)


if __name__ == '__main__':
    main()
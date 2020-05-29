import nltk
from nltk.tree import Tree
from nltk.draw import TreeView

from gramaticas import grammar1, grammar2, grammar3, grammar4, grammar5, grammar6

from PIL import Image

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

    return a[0]


def generarArbol(cadenaInput, gramatica, funcionSplit):

    cadena = funcionSplit(cadenaInput)

    arbol = gramaticaToArbol(cadena, gramatica)

    arbol.pretty_print()
    
    arbol.draw()

    # Bug si hay parentesis en los terminales de la gramatica
    t = Tree.fromstring(str(arbol))

    TreeView(t)._cframe.print_to_file('./res/output.ps')

    TARGET_BOUNDS = (1024, 1024)

    pic = Image.open('./res/output.ps')
    pic.load(scale=10)

    if pic.mode in ('P', '1'):
        pic = pic.convert("RGB")

    # Calculate the new size, preserving the aspect ratio
    ratio = min(TARGET_BOUNDS[0] / pic.size[0],
                TARGET_BOUNDS[1] / pic.size[1])
    new_size = (int(pic.size[0] * ratio), int(pic.size[1] * ratio))

    # Resize to fit the target size
    pic = pic.resize(new_size, Image.ANTIALIAS)

    # Save to PNG
    pic.save("./res/image.png")


def main():

    miGramatica = grammar5

    print("La gramatica seleccionada es:")
    print(miGramatica[1])

    cadenaInput = input("Ingrese cadena a validar: ")

    try:
        generarArbol(cadenaInput, miGramatica[0], splitCadena)

    except IndexError:

        print('La gramatica no genera la cadena ' + cadenaInput)

    except:

        try:
            generarArbol(cadenaInput, miGramatica[0], splitCadena2)

        except IndexError:

            print('La gramatica no genera la cadena ' + cadenaInput)
        
        except Exception as ex:

            print(ex)


if __name__ == '__main__':
    main()
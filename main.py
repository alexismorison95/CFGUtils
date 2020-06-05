import nltk
from nltk.tree import Tree
from nltk.draw import TreeView
from PIL import Image
import uuid
from gramaticas import lista_gramaticas



def split_cadena(word):
    """
    Funcion split simple para cuando la gramatica posee variables y terminales formados por un solo simbolo.\n
    Ej:\n
    S -> '(' L ')' | 'a' \n
    L -> L ',' S | S
    """

    return [char for char in word]


def split_cadena2(word):
    """
    Funcion split para cuando la gramatica posee variables y terminales formados por varios simbolos. \n
    Es necesario escribir la cadena a validar separando por espacios los simbolos y los terminales.\n
    Ej:\n
    S -> F S | F \n
    F -> 'FUNCTION' 'id' '(' P ')' C 'END' \n
    etc.
    """

    return word.split()


def gramatica_to_arbol(cadena, gramatica):
    a = []

    parser = nltk.ChartParser(gramatica)

    for tree in parser.parse(cadena):
        a.append(tree)

    return a[0]


def generar_png(file_name):
    TARGET_BOUNDS = (1024, 1024)

    pic = Image.open('./res/{}.ps'.format(file_name))
    pic.load(scale=10)

    if pic.mode in ('P', '1'):
        pic = pic.convert("RGB")

    # Calculate the new size, preserving the aspect ratio
    ratio = min(TARGET_BOUNDS[0] / pic.size[0],
                TARGET_BOUNDS[1] / pic.size[1])
    new_size = (int(pic.size[0] * ratio), int(pic.size[1] * ratio))

    # Resize to fit the target size
    #pic = pic.resize(new_size, Image.ANTIALIAS)

    # Save to PNG
    pic.save("./res/{}.png".format(file_name))


def generar_arbol(cadena_input, gramatica, funcion_split, file_name):

    cadena = funcion_split(cadena_input)

    arbol = gramatica_to_arbol(cadena, gramatica)

    arbol.pretty_print()

    print("El arbol se guarda en el archivo {}.ps".format(file_name))

    arbol.draw()

    # Bug si hay parentesis en los terminales de la gramatica
    t = Tree.fromstring(str(arbol))

    TreeView(t)._cframe.print_to_file('./res/{}.ps'.format(file_name))

    # No funciona en windows
    #generar_png(file_name)


def main():
    gramatica_selecccionada = lista_gramaticas[6]

    print("La gramatica seleccionada es:")
    print(gramatica_selecccionada[1])

    cadena_input = input("Ingrese cadena a validar: ")

    file_name = str(uuid.uuid4())

    try:
        generar_arbol(cadena_input, gramatica_selecccionada[0], split_cadena, file_name)

    except IndexError:

        print('La gramatica no genera la cadena ' + cadena_input)

    except:

        try:
            generar_arbol(cadena_input, gramatica_selecccionada[0], split_cadena2, file_name)

        except IndexError:

            print('La gramatica no genera la cadena ' + cadena_input)

        except Exception as ex:

            print(ex)


if __name__ == '__main__':
    main()

# CFGUtils

Programa muy básico y simple para graficar CFGs a partir de sus reglas, pasandole como imput el mismo y una palabra a validar.

Las gramáticas estan definidas en el archivo gramaticas.py y son de la siguiente forma:

```python
miGramatica = nltk.CFG.fromstring(
    """
    S -> '0' C | '1' B
    B -> '0' D | '1' S | 'e'
    C -> '0' S | '1' D
    D -> '0' B | '1' C
    """
)
```
> Una gramática se define como G = (V, T, P, S)
>
> V = Variables: S, B, C, D
>
> T = Terminales: 0, 1, e *(épsilon, Ɛ)*
>
> P = Producciones:S -> '0' C | '1' B
>
> S = Símbolo inicial: S


# Ejecución

Cuando se ejecuta el archivo main.py se le pide que ingrese una cadena a validar:
```
cadena = input("Ingrese cadena a validar: ")
```
Por ejemplo la cadena: **001e**

Luego se llama a la función gramaticaToArbol donde se le pasa como parámetros la cadena y la gramática importada:
```
arbol = gramaticaToArbol(cadena, miGramatica)
```
Luego se genera el arbol en una pantalla de Tkinter donde puede ver el resultado.

# Guardado del arbol

Cuando se ejecuta el programa se guarda en la carpeta **/res** un archivo llamado **output.ps**, aunque tambien puede guardar un archivo **.ps** desde la ventana de Tkinter.

Luego debe convertir el archivo **.ps** a **.png** con algun convertidor de archivos para obtener el siguiente resultado:

![Resultado.png](https://raw.githubusercontent.com/alexismorison95/CFGUtils/master/imagenes/output.png) 

-----

> **Bug**: Hay un bug si la gramática posee como terminales a los simbolos parentesis. La solución es no usar el archivo **.ps** generado automaticamente, sino guardar uno desde la ventana de Tkinter.
import nltk

# Simbolos entre comillas son terminales
# Letras en mayusculas son variables

grammar1 = nltk.CFG.fromstring(
    """
    S -> '(' L ')' | 'a'
    L -> L ',' S | S
    """
)

grammar2 = nltk.CFG.fromstring(
    """
    S -> '0' C | '1' B
    B -> '0' D | '1' S | 'e'
    C -> '0' S | '1' D
    D -> '0' B | '1' C
    """
)
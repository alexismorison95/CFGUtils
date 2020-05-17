import nltk

# Simbolos entre comillas son terminales
# Letras en mayusculas son variables

g1 = """
    S -> '(' L ')' | 'a'
    L -> L ',' S | S
    """
    
grammar1 = [nltk.CFG.fromstring(g1), g1]

############################################

g2 = """
    S -> '0' C | '1' B
    B -> '0' D | '1' S | 'e'
    C -> '0' S | '1' D
    D -> '0' B | '1' C
    """

grammar2 = [nltk.CFG.fromstring(g2), g2]

############################################

g3 = """
    S -> F S | F
    F -> 'FUNCTION' 'id' '(' P ')' C 'END'
    P -> 'id' ',' P | 'id' | 'e'
    C -> L ';' C | L ';'
    L -> EC ':' EA
    EC -> EA OR EA
    EA -> 'id' | 'CE' | EA OP EA | '(' EA ')'
    OP -> '+' | '-' | '*' | '/'
    OR -> '<' | '>' | '=' | '<>'
    """

grammar3 = [nltk.CFG.fromstring(g3), g3]

############################################
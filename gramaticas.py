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
    LF -> LF F | F
    F -> 'FUNCTION' 'id' '(' P ')' C 'END'
    P -> 'id' P | 'id' | 'e'
    C -> C S ';' | S ';'
    S -> EC ':' EA
    EC -> EA OR EA
    EA -> 'id' | 'CE' | EA OP EA | '(' EA ')' | 'id' '(' P ')'
    OP -> '+' | '-' | '*' | '/'
    OR -> '<' | '>' | '=' | '<>'
    """

grammar3 = [nltk.CFG.fromstring(g3), g3]

############################################

g4 = """
    LS -> LS S ';' | S ';' | 'e'
    S -> AS | C
    AS -> 'id' 'OA' EA
    EA -> 'id' | 'CE' | EA OP EA | '(' EA ')'
    OP -> '+' | '-' | '*' | '/'
    C -> 'if' CND 'then' LS 'else' LS 'end'
    CND -> EA OR EA
    OR -> '<' | '>' | '=' | '<>'
    """

grammar4 = [nltk.CFG.fromstring(g4), g4]

############################################

g5 = """
    LE -> LE EX ';' | EX ';'
    EX -> AS | LC | EP
    LC -> 'READ' '(' 'ID' ')'
    EP -> 'PRINT' '(' OPC ')'
    OP -> 'I' | 'U'
    EXT -> '{' LN '}' | '{' '}'
    LN -> 'NUM' ',' LN | 'NUM'
    COM -> '{' ID '}'
    AS -> 'ID' 'OA' OPC
    OPC -> 'ID' | OPC OP OPC | 'C' OPC | EXT | COM | '(' OPC ')' 
    """

grammar5 = [nltk.CFG.fromstring(g5), g5]
# ID OA { NUM , NUM } ; READ ( ID ) ; ID OA C ( ID I ID ) ; ID OA ID U ID ; PRINT ( ID ) ;

############################################

g6 = """
    LS -> LS S | S
    S -> AS ';' | PR ';' | RD ';' | EST 
    AS -> 'id' 'oa' OPS
    OPS -> 'id' | 'const' | '(' OPS ')' | OPS OPA OPS | 'id' '(' LP ')' | 'id' '(' ')'
    OPA -> '+' | '-' | '*' | '/'
    LP -> OPS ',' LP | OPS
    PR -> 'print' '(' OPS ')' | 'print' '(' 'texto' ')'
    RD -> 'read' '(' 'id' ')'
    EST -> CICL | COND
    CICL -> 'while' '(' EXPCOND ')'  '{' LS '}'
    COND -> 'if' '(' EXPCOND ')' '{' LS '}' ELSEIF
    ELSEIF -> 'else' '{' LS '}' | 'e'
    EXPCOND -> OPS OPR OPS | 'id' '(' LP ')' | 'id' '(' ')'
    OPR -> '<' | '>' | '==' | '<>' | '<=' | '>=' 
    """

grammar6 = [nltk.CFG.fromstring(g6), g6]

g7 = """
    S ->  S 'a' S  |   T
	T ->  'b' T | 'b' | S
    """

grammar7 = [nltk.CFG.fromstring(g7), g7]

############################################

lista_gramaticas = [grammar1, grammar2, grammar3, grammar4, grammar5, grammar6, grammar7]

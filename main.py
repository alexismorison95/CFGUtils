import nltk
import os
from nltk.tree import Tree
from nltk.draw import TreeView
from PIL import Image
import io

grammar2 = nltk.CFG.fromstring("""
    S -> '0' C | '1' B
    B -> '0' D | '1' S | 'e'
    C -> '0' S | '1' D
    D -> '0' B | '1' C
""")

grammar1 = nltk.CFG.fromstring("""
    S -> '(' L ')' | 'a'
    L -> L ',' S | S
""")

def split2(word): 
    return [char for char in word]  

def parse(sent):

    #Returns nltk.Tree.Tree format output
    a = []  
    parser = nltk.ChartParser(grammar1)

    for tree in parser.parse(sent):
        a.append(tree)
    return(a[0]) 

sentence = split2('(a,(a,(a),(a,a)))')

#Gives output as structured tree   
print(parse(sentence))

#Gives tree diagrem in tkinter window
parse(sentence).draw()

t = Tree.fromstring(str(parse(sentence)))

TreeView(t)._cframe.print_to_file('./res/output.ps')

os.system('convert output.ps output.png')

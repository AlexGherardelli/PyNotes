# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 12:43:26 2022

@author: alessandra.gherardel
"""

#%% Initialize Binary Tree

class BinaryTree:
    def __init__(self, value, left = None, right = None):
        self.left = left
        self.right = right
        self.value = value
        
    def __str__(self, lev=0):
        "torno una stringa che rappresenta l'albero indentando i sottoalberi"
        tab = "   "*lev     # lev di indentazione corrente
        risultato = f"{tab}BinaryTree( {self.value} )"
        if self.left:
            risultato += f"\n{self.left.__str__(lev+1)}"
        else:
            risultato += f"\n{tab}   None"
        if self.right:
            risultato += f"\n{self.right.__str__(lev+1)}"
        else:
            risultato += f"\n{tab}   None"
        return risultato
        
n1 = BinaryTree(1)
n2 = BinaryTree(2, n1)
n3 = BinaryTree(3)
n4 = BinaryTree(4)
n5 = BinaryTree(5,n2)
n6 = BinaryTree(6,n3,n4)
n7 = BinaryTree(7,n5,n6)


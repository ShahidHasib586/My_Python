# -*- coding: utf-8 -*-
"""
Created on Sun May 15 23:56:25 2022

@author: shahi
"""

#scope function = the region that a ariable is created, a variable is only available from inside the region it is created, a local or globally scoped version of a varibale can be created 

def display_name():
    name = "code"
    print(name)    #local sope only recognised inside the disply_name function

#global variable = is know to have a global scope

name = "bro"
display_name()
print(name)

#local
#global
#L_E_G_B rules
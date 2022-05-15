# -*- coding: utf-8 -*-
"""
Created on Sun May 15 23:35:34 2022

@author: shahi
"""

#keyword Argyments

def hello(first, middle, last):
    print("Hello " +first+" "+middle+" "+last)
hello ("code", "dute", "bro")
#keyword argument

def hello(first, middle, last):
    print("Hello " +first+" "+middle+" "+last)
hello ( middle="dute", last="bro",first="code")
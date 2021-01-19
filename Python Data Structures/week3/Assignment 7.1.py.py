# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 00:10:54 2020

@author: snsenel
"""
fname = input('Enter file name: ')
fh = open(fname)
print(fh.read().upper().strip()) #or for lx in fh: ly=lx.rstrip() print(ly.upper())


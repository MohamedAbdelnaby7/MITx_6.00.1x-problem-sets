# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 20:42:09 2021

@author: moham
"""

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    flat_list = []
    
    for sublist in aList:
        if not (isinstance(sublist, list)):
            flat_list.append(sublist)
        else:
            flat_list.extend(flatten(sublist))
    return flat_list
            
ALIST = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flat_list = flatten(ALIST)
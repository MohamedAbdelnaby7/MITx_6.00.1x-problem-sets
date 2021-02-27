# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def printMove(frm, to):
    print('movr from '+ frm+ ' to ' + to)
def hanoi_tower(n, frm_pole, to_pole, aux_pole):
    if n == 1:
        printMove(frm_pole, to_pole)
    else:
        hanoi_tower(n-1, frm_pole, aux_pole, to_pole)
        hanoi_tower(1, frm_pole, to_pole, aux_pole)
        hanoi_tower(n-1, aux_pole, to_pole, frm_pole)


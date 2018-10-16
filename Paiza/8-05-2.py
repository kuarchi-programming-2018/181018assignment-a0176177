# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 15:48:05 2018

@author: makoto
"""

class Gakusei:
    def __init__(self, kokugo, sansu):
        self.kokugo = kokugo
        self.sansu  = sansu

    def sum(self):
        return self.kokugo + self.sansu

yamada = Gakusei(70, 43)
print("合計は" + str(yamada.sum()) + "点です")
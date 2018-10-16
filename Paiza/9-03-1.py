# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 22:05:07 2018

@author: makoto
"""

class Greeting:
    def __init__(self):
        self.msg = "hello"
        self.target = "paiza"

    def say_hello(self):
        print(self.msg + " " + self.target)

class Hello(Greeting):
    def say_hello(self, target):
        print(self.msg + " " + target)


player = Hello()
player.say_hello("python")
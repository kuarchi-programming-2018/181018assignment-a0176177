# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 15:23:00 2018

@author: makoto
"""

points={"国語":70,"算数":35,"英語":52}
sum=0
for key in points:
    sum+=points[key]
print(int(sum))
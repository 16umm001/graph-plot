#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Sat Aug 11 12:58:45 2018
    @author: adarsh
    """

import matplotlib.pyplot as plt
x = [int(i) for i in input('Enter x-axis value :').split()]
y = [int(i) for i in input('Enter y-axis value :').split()]
print(x)
print(y)
plt.plot(x,y, color='red')
plt.xlabel('x-axis ')
plt.ylabel('y-axis')
plt.title('Graph')
plt.show()

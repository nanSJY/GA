# -*- coding: UTF-8 -*-
'''
Created on 2017年1月16日

@author: Python
'''
from math import sin

# a = [0,1,2,3,3,2]
# b = [2,2,2,2,2,2]
p = [i/100. for i in range(1000)]
a = [i*sin(3.14*i)+2 for i in p]
b = [0 for i in range(1000)]
# b = [i+1 for i in range(10)]
duration = len(a) - 1
timebin = 1
points = pow( duration+1,2)



#根据points求解二进制编码的长度
def getLength(points):
    n = 1
    total = 0
    while total < points:
        total = pow(2,n)
        n += 1
    return n-1  

chrom_length = getLength(points)
pop_size = 500
pc = 0.8
pm = 0.1
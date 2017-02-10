# -*- coding: UTF-8 -*-
'''
Created on 2017年1月16日

@author: Python
'''

import random

from trans.para import duration
from trans.para import pop_size
from trans.para import chrom_length
from trans.para import points
from trans.encode import real_to_bin

# 初始化：随机产生pop_size个个体，返回 二进制串
def initialize(size = pop_size,length = chrom_length):
    real = random.sample([i for i in range(points)],size)
    pop = []
    for i in real:
        pop.append(real_to_bin(i))
    return pop


if __name__ == '__main__':
    pop = initialize()
    print 'len=',len(pop)
    for i in pop:
        print int(i,2)
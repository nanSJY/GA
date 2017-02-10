# -*- coding: UTF-8 -*-
'''
Created on 2017年1月17日

@author: Python
'''

import numpy as np

from trans.para import pc,chrom_length

def crossover(pop,proc=pc):
    for i in [i for i in range(0,len(pop)-1,2)]:
        p = np.random.random()
        if p < proc:
            index = np.random.randint(0,chrom_length)
            p = pop[i][index:]
            pop[i] = pop[i][0:index] + pop[i+1][index:]
            pop[i+1] = pop[i+1][0:index] + p
    return pop

if __name__ == '__main__':
    pop = ['000000','000001','001000','001001']
    print pop
    print crossover(pop,1)
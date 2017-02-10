# -*- coding: UTF-8 -*-
'''
Created on 2017年1月17日

@author: Python
'''
import numpy as np
from trans.para import pm,chrom_length

def mutation(pop,prom=pm):
    for i in range(len(pop)):
        individual = pop[i]
        p = np.random.random()
        if p < prom:
            index = np.random.randint(0,chrom_length)
            individual = list(individual)
            if individual[index] == '0':
                individual[index] = '1'
            else:
                individual[index] = '0'
            individual = ''.join(individual)
            pop[i] = individual
    return pop 

if __name__ == '__main__':
    pop = ['000000','000001','001000','001001']
    print pop
    print mutation(pop, 1)
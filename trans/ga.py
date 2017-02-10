# -*- coding: UTF-8 -*-
'''
Created on 2017年1月16日

@author: Python
'''
import matplotlib.pyplot as plt

from trans.initialize import initialize
from trans.fit import get_fitValue
from trans.encode import geneDecoding,pop_geneDecoding
from trans.selection import selection, best_individual
from trans.mutation import mutation
from trans.crossover import crossover

if __name__ == '__main__':
    pop = initialize()
    arg = []

    count = 30
    for i in range(count):
        print 'i=',i    
        pop = selection(pop)
        pop = crossover(pop)
        pop = mutation(pop)
        fitValue = get_fitValue(pop)
        arg.append( float(sum(fitValue)) / len(fitValue))

    best = best_individual(pop)
    print geneDecoding(best)
    print get_fitValue([best,])

    fig = plt.figure(1)  
    ax = fig.add_subplot(111)  
    DataX = [i for i in range(count)]  
    DataY = arg
    ax.scatter(DataX,DataY) 
    plt.show()
    
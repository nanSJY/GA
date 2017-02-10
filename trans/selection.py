# -*- coding: UTF-8 -*-
'''
Created on 2017年1月17日

@author: Python
'''
import numpy as np

from trans.fit import get_fitValue
from trans.initialize import initialize
from trans.para import chrom_length

# 找出适应度最高的个体，保留该基因型到下一代，确保种群不会退化
# 输入 pop的适应度值list，返回 基因型，二进制串
def best_individual(pop):
    fit = get_fitValue(pop)
    index = fit.index(max(fit))
#     return (index,pop[index])
    return pop[index]

# 查找适应度为 负值和0 的基因型
def worst_individual(pop):
    fit = get_fitValue(pop)
    worst = []
    for i in range(len(fit)):
        if fit[i] <= 0 :
#             worst.append((i,pop[i]))
            worst.append(pop[i])            
    return worst

def selection(pop):
    best = best_individual(pop)
    worst = worst_individual(pop)
    pop.remove(best)
    for i in range(len(worst)):
        if worst[i] in pop:
            pop.remove(worst[i])
        
    pop = roulette_sel(pop)
    pop.append(best)
    pop.extend(initialize( len(worst), chrom_length))
    return pop

def get_pro(fit):
    sum = np.sum(fit)
    if np.sum(fit) == 0:
        return fit
    for i in range(len(fit)):
        fit[i] = float(fit[i])/sum
        if i != 0:
            fit[i] += fit[i-1]
    return fit

def roulette_sel(population):
    fitValue = get_fitValue(population)
    pro = get_pro(fitValue)
    sel_pop = []
    for i in range(len(population)):
        value = np.random.random()
        j = 0
        while(value > pro[j]):
            j += 1
        sel_pop.append(population[j])
    return sel_pop


if __name__ == '__main__':
    pop = ['000000','000001','001000','001001']
    print selection(pop)
#     fitValue = [3,5,6,1,2,1]
#     print get_pro(fitValue)
#     print initialize(0, 8)
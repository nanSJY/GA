# -*- coding: UTF-8 -*-
'''
Created on 2017年1月16日

@author: Python
'''

from trans.para import a,b
from trans.para import duration
from trans.para import timebin
from trans.encode import geneDecoding

def get_fitValue(pop):
    fitValue = []
    for p in pop:
        (d,w) = geneDecoding(p)
        if w == 0 or  (w+d) > duration:
            fitValue.append(0)
        else:
            s = 0
            for i in range(w):
                s += ( a[d+i] + a[d+i+1] - b[d+i] - b[d+i+1] )*timebin
            fitValue.append(s)
    return fitValue



if __name__ == '__main__':
    pop = ('0000','0001','1110')
    a = get_fitValue(pop)
    print pop
    print a
# -*- coding: UTF-8 -*-
'''
Created on 2017年1月16日

@author: Python
'''

from trans.para import duration
from trans.para import chrom_length

# 基因编码：坐标 -- 实数 -- 二进制string XXXX (等长码，长度为chrome_length)
def geneEncoding(w,d,chrom_length):
    real = w*(duration+1)+d
    bit = real_to_bin(real)
    return bit

def real_to_bin(real):
    return '{:0>{length}}'.format(bin(real)[2:],length = chrom_length)

# 解码：二进制 -- 坐标
def geneDecoding(bits):
    real = int(bits,2)
    w = real / (duration+1)
    d = real - w*(duration+1)
    return (d,w)

def pop_geneDecoding(pop):
    code = []
    for bits in pop:
        code.append(geneDecoding(bits))
    return code

if __name__ == '__main__':
    l = []
    for i in range(duration+1):
        for j in range(duration+1):
            l.append(geneEncoding(i, j, chrom_length))
    for x in l:
        print geneDecoding(x)   
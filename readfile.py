#!/usr/bin/env python3
from collections import defaultdict


def readlessondata(filename):
    lessondata = defaultdict(list)
    f = open(filename, 'r', encoding='utf-8')
    x = f.readline()
    x = f.readline()
    while len(x) > 0:
        data = x.strip().split('\t')
        lessondata[data[-2]] += (data[:-2] + data[-1:])
        x = f.readline()
    return lessondata

print(readlessondata('Algo_Project_data.txt'))
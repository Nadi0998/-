#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)
data3 = gen_random(1,9,15)
data = ['a', 'A', 'b', 'B']

# Реализация задания 2
for i in Unique(data1):
   print(i, end=', ')
print()
#for i in data2:
#   print(i, end=', ')
#print()
for i in Unique(data2):
   #print('a')
   print(i, end = ', ')
print()
for i in Unique(data3):
   #print('a')
   print(i, end = ', ')
print()
for i in Unique(data):
   print(i, end=', ')
print()
for i in Unique(data, ignore_case=True):
   print(i, end=', ')

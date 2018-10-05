#!/usr/bin/env python3
import math
data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
# Реализация задания 3
def sorted(items):
    n = 1
    while n < len(items):
        for i in range(len(items) - n):
            if math.fabs(items[i]) > math.fabs(items[i + 1]):
                items[i], items[i + 1] = items[i + 1], items[i]
        n += 1
    return items


data1 = sorted(data)
print(data1)
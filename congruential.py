def LCG(seed, n, a=4, c=3, m=10000):
    numbers = []
    for i in xrange(n):
        seed = (a * seed + c) % m
        numbers.append(seed)

    return numbers

list =  LCG(5, 100)
print list

import collections
print [item for item, count in collections.Counter(list).items() if count > 1]
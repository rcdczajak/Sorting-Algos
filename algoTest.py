from algorithms import Sorting
import random

n = 50
l = [ ]

for i in range (n):
    l.append (random.randint (0, n * 2))

print (l)
l = Sorting.defaultSort (l)
print (l)
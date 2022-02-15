from itertools import *
a = sorted(''.join(i) for i in product('ПОРТ', repeat=5))
print(a)
print(a.index('ТОПОР') - a.index('РОПОТ') + 1)
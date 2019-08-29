import bisect
import random

random.seed(1)

print('New  Pos  Contents')
print('---  ---  --------')

l = []
for i in range(1, 15):
    r = random.randint(1, 100)
    position = bisect.bisect(l, r)
    bisect.insort(l, r)
    print('%3d %3d %s' % (r, position, l))

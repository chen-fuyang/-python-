import time
#引出生成器;
#创建生成器: 1、通过列表生成式来创建

g = (x for x in range(1,10))
next(g)
'''
print(next(g))
print(next(g))
print(next(g))
time.sleep(5)
print(next(g))
print(next(g))
print(next(g))
print(next(g))


for i in g:
    print(i,'-----')
'''

g2 = (x for x in range(10) if x%2==0)
print(next(g2))
print(next(g2))
print(next(g2))
print(next(g2))
print(next(g2))
print(next(g2))
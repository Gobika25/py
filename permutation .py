from itertools import permutations
n=input()
p=permutations(n)
for i in list(p):
    x=''.join(i)
print(x,end='')
i/p:1234
o/p:4321

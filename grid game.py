a=int(input())
l=[]
p=[]
k=[]
for i in range(0,a):
    l.append(list(map(int,input().split(" "))))
for i in range(len(l)):
    p.append(l[i][0])
    k.append(l[i][1])
h=min(p)*min(k)
print(h)
i/p:3
2 3
3 7
4 1
o/p:2

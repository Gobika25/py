a=int(input())
l=[]
d=0
b=[]
v=[]
for i in range(2,a):
    if i > 1:
        for j in range(2,(i//2)+1):
            if i%j==0:
                break
        else:
            l.append(i)
               
for i in range(len(l)):
    d=d+l[i]
    if d>l[0]:
        b.append(d)
for j in b:
    if j in l:
        v.append(j)
print(len(v))



ip:20

op:2

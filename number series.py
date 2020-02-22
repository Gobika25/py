a=int(input())
b=list(map(int,input().split(" ")))
l=[]
p=sum(b)
for i in range(0,len(b)):
    l.append(p-b[i])
for j in l:
    print(j,end=" ")

a=int(input())
b=list(map(str,input().split(" ")))
c=int(input())
l=[]
for i in range(len(b)-c,len(b)):
    l.append(b[i])
for j in range(0,len(b)-c):
    l.append(b[j])
print(l)
    

a,b=map(int,input().split(" "))
c=0
d=0
for i in range(a,b+1):
    c=0
    temp=i                      
    lst=0
    l=len(str(i))
    while(i>0):
        lst=i%10
        i=i//10
        c+=lst**l
    if c==temp:
        print(c)
        d+=1
if d==0:
    print("NO")
    i/p:20 1700
    o/p:
    153
    370
    371
    407
    1634

a=list(map(str,input().split(" ")))
n=len(a)
for i in range(0,n):
    for j in range(i+1,n):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
for i in range(0,n):
    print(a[i],end=" ")
    i/p:7654321
    o/p:1234567

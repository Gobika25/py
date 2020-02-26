r,c=map(int,input().split(" "))
b=[[0 for i in range(r)] for j in range(c)]
b1=[[0 for i in range(r)] for j in range(c)]
d=[[0 for i in range(r)] for j in range(c)]
for i in range(0,r):
    for j in range(0,c):
        b[i][j]=int(input())
for i in range(0,r):
    for j in range(0,c):
        b1[i][j]=int(input())
for i in range(r):
    for j in range(c):
        for k in range(r):
            d[i][j]+=(b[i][k]*b1[k][j])
for i in range(r):
    for j in range(c):
        print(d[i][j],end=" ")
    print(" ")

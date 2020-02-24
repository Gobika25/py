r,c=map(int,input().split())
matrix=[]
for i in range(r):
   m=[]
   for j in range(c):
       m.append(int(input()))
   matrix.append(m)
for i in range(r):
       for j in range(c):
           print(matrix[i][j],end=" ")
       print()
       

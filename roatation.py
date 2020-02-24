a=input()
d=int(input())
lf=a[0:d]
ls=a[d:]
rf=a[0:len(a)-d]
rs=a[len(a)-d:]
print("Left Rotetaion: ",(ls+lf))
print("Right Roteation: ",(rs+ls))

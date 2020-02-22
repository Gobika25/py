a=input()
c=0
for i in a:
    if i=='{':
        c+=1
    elif i=='(':
        c+=1
    elif i=='[':
        c+=1
    elif i==']':
        c-=1
    elif i==')':
        c-=1
    elif i=='}':
        c-=1
if c==0 :
    print("Balanced")
else:
    print("Un Balanced")
    
    i/p:{([])}
    o/p:Balanced

a = int(input())
for i in range(a):
    b = int(input())
    height = 1
    for i in range(b):
        if i % 2 == 0:
            height *= 2
        else:
            height += 1
            
    print(height)
    
    
    
    input:3
    0
    1
    4
     outpu:
     1
     2
     7

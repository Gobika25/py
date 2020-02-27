def po(a):
    i=1
    while(i<=10):
        t=a*i
        yield t
        i+=1
k=po(2) #k is a generator object
for i in range(10):
    print(next(k)) #next() is the generator

class Cse:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def swap(self):
        self.a,self.b=self.b,self.a 
a,b=32,56
p=Cse(a,b)
Cse.swap(p)
print(p.a,p.b)


or  


class Cse: #swap metod 2
    def swap(self,a,b):
        self.a=a
        self.b=b
        self.a,self.b=self.b,self.a
a,b=32,56
p=Cse()
Cse.swap(p,a,b) #p.swap(a,b)
print(p.a,p.b)

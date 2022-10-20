from itertools import count


class Parent:
    count = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        Parent.count+=1

    def __str__(self):
        return 'Name: {}, Age: {}'.format(self.name,self.age)

p1 = Parent("João",10)
p2 = Parent ("Maria",11)
p3 = Parent ("Nathan formigão",24)
p4 = Parent ("Erick Philco",32)

print (p1)
print(p2)
print(p3)
print(p4)
print("Quantidade de parentes: ",Parent.count)
    
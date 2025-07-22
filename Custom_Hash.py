class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __hash__(self):
        return hash(self.name) ^ hash(self.age)
    
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age
    
p1 = Person("Alice", 30)
p2 = Person("Bob", 25)

print(hash(p1))
print(hash(p2))
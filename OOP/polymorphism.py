class Animal:
    def move(self):
        pass

class Cat(Animal):
    def move(self):
        return "Walking"

class Bird(Animal):
    def move(self):
        return "Flying "

class Fish(Animal):
    def move(self):
        return "Swimming"

# Example 
animals = [Cat(), Bird(), Fish()]

for animal in animals:
    print(f"{animal.__class__.__name__}: {animal.move()}")

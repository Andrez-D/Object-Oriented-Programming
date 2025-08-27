# Base class: Animal
class Animal:
    def __init__(self, name, age):
        self.name = name      # public attribute
        self._age = age       # protected attribute (convention)
    
    def move(self):
        print(f"{self.name} moves in a general way.")

    # Getter for age (encapsulation)
    def get_age(self):
        return self._age
    
    # Setter for age (can include validation)
    def set_age(self, new_age):
        if new_age >= 0:
            self._age = new_age
        else:
            print("Invalid age")

# Derived class Dog
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    
    def move(self):
        print(f"{self.name} runs energetically.")

# Derived class Bird
class Bird(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan  # in cm
    
    def move(self):
        print(f"{self.name} flies gracefully in the sky.")


# Demonstration of classes and polymorphism

dog1 = Dog("Buddy", 3, "Labrador")
bird1 = Bird("Tweety", 2, 25)

dog1.move()   # Overrides Animal.move() - prints: Buddy runs energetically.
bird1.move()  # Overrides Animal.move() - prints: Tweety flies gracefully in the sky.

print(f"{dog1.name} is {dog1.get_age()} years old.")
dog1.set_age(4)
print(f"{dog1.name} is now {dog1.get_age()} years old.")

# Invalid age demonstration
dog1.set_age(-1)  # Will print "Invalid age"

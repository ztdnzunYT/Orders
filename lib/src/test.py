class Dog:
    def __init__(self, name, age):
        self.name = name  # Assign the name attribute
        self.age = age    # Assign the age attribute

    def bark(self):
        print(f"{self.name} says woof!")

# Create an instance of the Dog class
my_dog = Dog("Buddy", 3)

# Access attributes and methods
print(my_dog.name)  # Output: Buddy
print(my_dog.age)   # Output: 3
my_dog

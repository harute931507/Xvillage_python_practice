class Animal:
    feet_number = 4

    def shout(self):
        print("Hello! I am a animal .")

class Dog(Animal):
    pass

dog = Dog()
dog.shout()
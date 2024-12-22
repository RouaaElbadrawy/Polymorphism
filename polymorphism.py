# Polymorphism 

class Animal:
    def make_sound(self):
        print("AAnimAl makes sound")
        
class Dog(Animal): 
    def make_sound(self):
        print("Dogs Bark")
        
        
class Bear(Animal): 
        def make_sound(self):
            print("Bears Growl")
            
class Horse(Animal): 
        def make_sound(self):
            print("Horse Neigh.")
            

animal = Animal()
animal.make_sound() 

dog = Dog()
dog.make_sound()

bear = Bear()
bear.make_sound() 

horse = Horse()
horse.make_sound() 
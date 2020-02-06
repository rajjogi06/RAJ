#DOGS

class Dog:

    #CLASS ATTRIBUTE
    species = 'mamma1'

    #INITIALIZER/INSTANCE ATTRIBUTES
    def __init__(self,name,age):
        self.name = name
        self.age = age


    # INSTANCE METHOD
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    #INSTANCE METHOD
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

#INSTANTIATE THE DOG OBJECT
mikey = Dog("Mikey", 6)

#CALL OUR INSTANCE METHODS
print(mikey.description())
print(mikey.speak("GRUFF GRUFF"))
        

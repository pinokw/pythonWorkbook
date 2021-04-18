# Aufgabenstellung: Die allgemeine "Person-Class" soll eine Untergruppe (Byby) beinhalten. 
# Hierbei soll die Baby Class alle Attribute von der Parent-Class erben allerdings
#soll das child-object dennoch andere Eigenschaften haben

class Person: 

    description="General Person"
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def speak(self):
        print("My name ist {} and I am {} years old.".format(self.name, self.age))

    def eat(self, food):
        print ("{} eats {}.".format(self.name, food))

    def action(self):
        print("{} jumps.".format(self.name))

class Baby(Person): # inherits initilistion of Person class
    description="baby" #description wird überschrieben

    def speak(self): #speak wird überschrieben
        print("ba ba ba ba ba")
    
    def nap(self):
        print("{} takes an nap".format(self.name))

person=Person("Steve", 20)
person.speak()
person.eat("pasta")
person.action()

baby=Baby("Carl", "1")
baby.speak()
baby.action()

print(isinstance(Baby, Person)) # see it baby is a Person

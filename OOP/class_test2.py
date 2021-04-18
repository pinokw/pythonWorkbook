class human:

    species="Säugetier"
    children=0

    def __init__(self, gender, age, ethnic): # initiatior of instance (gilt nicht für die gesamte klasse)
        self.gender=gender
        self.age=age
        self.ethnic=ethnic

    def person(self):
        return male(self.age, self.ethnic, self.children)

    class male:

        def __init__(self, age2, ethnic2, children2):
            self.age=age2
            self.ethnic=ethnic2
            self.children=children2
    

x=input("Gender :")
y=input("Age :")
z=input("Ethnic :")

h=human(x, y, z)
print ("You entered a {} gender {} with the age of {} and {} race.".format(h.species, h.gender, h.age, h.ethnic))
human.age
print (y.age)

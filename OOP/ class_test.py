from tkinter import *

class Dog:

    species='mammal' # class attribute (gilt für die gesamte klasse)

    def __init__(self, name, age): # initiatior of instance (gilt nicht für die gesamte klasse)
        self.name=name
        self.age=age

    def lebens_erw(self, age):
        if int(age)>15:
            self.lebens_erw="gering"
        else:
            self.lebens_erw="hoch"

root = Tk()
root.title('Titel')
root.geometry('500x500')
global dog_list
dog_list=[]

def berechnen():
    name1=input_name.get()
    age1=input_age.get()
    dog=Dog(name1, age1)
    dog_list.append(dog)
    input_name.delete(0, "end")
    input_age.delete(0, "end")

def show_dogs():
    dogs=""
    for item in dog_list:
        # print(item.name)
        dogs += "Der Hund {} ist ein {} und ist {} Jahre alt. Seine Lebenserwartung ist {} .".format(item.name, item.species, item.age, item.lebens_erw(item.age)) + "\n"
    out_txt=Text(output_frame)
    out_txt.pack(padx=5, pady=5)
    out_txt.insert(END, dogs)

#Frame
input_frame=LabelFrame(root, text="Input").pack()
output_frame=LabelFrame(root, text='Output').pack()
label1=Label(input_frame, text="Name des Hundes").pack(padx=5, pady=5)
input_name=Entry(input_frame)
input_name.pack()
label2=Label(input_frame, text="Alter des Hundes").pack(padx=5, pady=5)
input_age=Entry(input_frame)
input_age.pack()
button=Button(input_frame, text="Add Dog", command=berechnen).pack()
button=Button(input_frame, text="Show Dogs", command=show_dogs).pack()


root.mainloop()

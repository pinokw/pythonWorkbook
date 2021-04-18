from tkinter import *

root=Tk()
root.geometry('500x500')

class Elder:
    def __init__(self, master): # master ist der root - nur ein anderer Name
        my_frame=Frame(master)
        my_frame.pack()
        self.my_button=Button(master, text="Click Me", command=self.clicker)
        self.my_button.pack(pady=5, padx=5)

    def clicker(self):
        g=Output(root, "you clicked it")

class Output:   
    def __init__(self, master, text): # master ist der root - nur ein anderer Name
        self.label1=Label(master, text=text)
        self.label1.pack(pady=5, padx=5)


    
e=Elder(root)
f=Output(root, "the")

root.mainloop()
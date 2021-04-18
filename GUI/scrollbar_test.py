from tkinter import *

root = Tk()

root.title('Titel')
#root.iconbitmap('c:/location)
root.geometry('500x500')

from tkinter import ttk

# create a main frame1
main_frame=Frame(root)
main_frame.pack(fill=BOTH, expand=1)

# create a canvas (graphical frame, expands from top left to lower right)
my_canvas= Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# add scrollbar to canvas
my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
#scrollbar in main frame aber gelinkt zum canvas (yview=vertical)
my_scrollbar.pack(side=RIGHT, fill=Y)

#configure canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

# create another frame2 in the canvas
second_frame=Frame(my_canvas)

# add frame2 ro window in canvas
my_canvas.create_window((0,0), window=second_frame, anchor="nw")

for thing in range(0, 100):
    myButton=Button(second_frame, text=f'Botton {thing}')
    myButton.pack()



root.mainloop()
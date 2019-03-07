#cody dzierzon
#3/5/19

from tkinter import *
from tkinter import font

root = Tk()
root.title("lAZY buttons")
root.geometry("200x85")
root.configure(bg = "Red")

app= Frame(root)
app.grid()
app.configure(bg = "green")


bttn1 = Button(app, text = "Shazzzzaaam")
bttn1.grid()

bttn2 = Button(app)
bttn2.grid()
bttn2.configure(text = "don't click here")
bttn2.configure(bg = 'yellow')
bttn2.configure(fg = "red")

bttn3 = Button(app)
bttn3.grid()
bttn3["text"]= "Kablam"



root.mainloop()
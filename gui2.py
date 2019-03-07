



from tkinter import *


class Application(Frame):

    def __init__(self, master):
        """Initialize the Frame"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.bttn1 = Button(self, text="Shazzzzaaam")
        self.bttn1.grid()

        self.bttn2 = Button(self)
        self.bttn2.grid()
        self.bttn2.configure(text="don't click here")
        self.bttn2.configure(bg='yellow')
        self.bttn2.configure(fg="red")

        self.bttn3 = Button(self)
        self.bttn3.grid()
        self.bttn3["text"] = "Kablam"
        self.bttn3["bg"] = "Blue"
        self.bttn3["fg"] = "Green"

root = Tk()
root.title("Click Counter")
root.geometry("200x100")
app = Application(root)

root.mainloop()
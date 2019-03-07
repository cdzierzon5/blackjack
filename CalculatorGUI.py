#Cody Dzierzon
#3/7/19

from tkinter import *

class Application(Frame):
    "GUI application which is a calculator"
    def __init__(self, master):
        """Initialize the Frame"""
        super(Application, self).__init__(master)
        self.grid()
        self.lbl_total = 0
        self.create_widget()
    def create_widget(self):
        """creates buttons"""
        self.lbl= Label(self, text = "Calculator")
        self.lbl.grid(row = 0, column = 5, columnspan = 1, sticky = W)

        self.ent = Entry(self)
        self.lbl = Label(self, text="")
        self.lbl.grid(row=0, column=0, sticky=W)
        self.ent.grid(row=1, column=5, sticky=W)

        self.bttn = Button(self)
        self.bttn['text'] = "9"
        self.bttn.grid(row=2, column=0, sticky=S)
        self.bttn.configure(bg='light green')
        self.bttn.configure(fg='dark green')

        self.bttn = Button(self)
        self.bttn['text'] = "8"
        self.bttn.grid(row=2, column=1, sticky=S)
        self.bttn.configure(bg='light green')
        self.bttn.configure(fg='dark green')

        self.bttn = Button(self)
        self.bttn['text'] = "7"
        self.bttn.grid(row=2, column=2, sticky=S)
        self.bttn.configure(bg='light green')
        self.bttn.configure(fg='dark green')

        self.bttn = Button(self)
        self.bttn['text'] = "6"
        self.bttn.grid(row=3, column=0, sticky=S)
        self.bttn.configure(bg='light green')
        self.bttn.configure(fg='dark green')

        self.bttn = Button(self)
        self.bttn['text'] = "5"
        self.bttn.grid(row=3, column=1, sticky=S)
        self.bttn.configure(bg='light green')
        self.bttn.configure(fg='dark green')

        self.bttn = Button(self)
        self.bttn['text'] = "4"
        self.bttn.grid(row=3, column=2, sticky=S)
        self.bttn.configure(bg='light green')
        self.bttn.configure(fg='dark green')

        self.bttn = Button(self)
        self.bttn['text'] = "3"
        self.bttn.grid(row=4, column=0, sticky=S)
        self.bttn.configure(bg='light green')
        self.bttn.configure(fg='dark green')

        self.bttn = Button(self)
        self.bttn['text'] = "2"
        self.bttn.grid(row=4, column=1, sticky=S)
        self.bttn.configure(bg='light green')
        self.bttn.configure(fg='dark green')

        self.bttn = Button(self)
        self.bttn['text'] = "1"
        self.bttn.grid(row=4, column=2, sticky=S)
        self.bttn.configure(bg='light green')
        self.bttn.configure(fg='dark green')

        self.bttn = Button(self)
        self.bttn['text'] = "0"
        self.bttn.grid(row=5, column=1, sticky=S)
        self.bttn.configure(bg='light green')
        self.bttn.configure(fg='dark green')

        #Operators
        self.bttn = Button(self)
        self.bttn['text'] = "+"
        self.bttn["command"] = self.add_count
        self.bttn.grid(row=2, column=3, sticky=S)
        self.bttn.configure(bg='violet')
        self.bttn.configure(fg='light green')

        self.bttn = Button(self)
        self.bttn['text'] = "-"
        self.bttn["command"] = self.sub_count
        self.bttn.grid(row=3, column=3, sticky=S)
        self.bttn.configure(bg='violet')
        self.bttn.configure(fg='light green')

        self.bttn = Button(self)
        self.bttn['text'] = "/"
        self.bttn["command"] = self.div_count
        self.bttn.grid(row=4, column=3, sticky=S)
        self.bttn.configure(bg='violet')
        self.bttn.configure(fg='light green')

        self.bttn = Button(self)
        self.bttn['text'] = "x"
        self.bttn["command"] = self.mult_count
        self.bttn.grid(row=5, column=3, sticky=S)
        self.bttn.configure(bg='violet')
        self.bttn.configure(fg='light green')

        self.bttn = Button(self)
        self.bttn['text'] = "="
        self.bttn["command"] = self.equal_count
        self.bttn.grid(row=6, column=3, sticky=S)
        self.bttn.configure(bg='violet')
        self.bttn.configure(fg='light green')


    def add_count(self):
        pass
    def sub_count(self):
        pass
    def div_count(self):
        pass
    def mult_count(self):
        pass
    def equal_count(self):
        pass

root = Tk()
root.title("Click Counter")
root.geometry("250x175"
              "")
app = Application(root)

root.mainloop()

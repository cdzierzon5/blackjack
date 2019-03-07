from tkinter import *

class Application(Frame):
    "GUI application which counts button clicks"
    def __init__(self, master):
        """Initialize the Frame"""
        super(Application, self).__init__(master)
        self.grid()
        self.lbl_total = 0
        self.create_widget()
    def create_widget(self):
        """create button which displays number of clicks"""
        self.lbl= Label(self, text = "Count")
        self.lbl.grid()

        self.lbl= Label(self, text = self.lbl_total)
        self.lbl.grid()

        self.bttn = Button(self)
        self.bttn['text'] = "+"
        self.bttn["command"] = self.add_count
        self.bttn.grid()
        self.bttn.configure(bg='black')
        self.bttn.configure(fg='red')

        self.bttn2 = Button(self)
        self.bttn2['text'] = "-"
        self.bttn2["command"] = self.sub_count
        self.bttn2.grid()
        self.bttn2.configure(bg='black')
        self.bttn2.configure(fg='orange')

        self.bttn3 = Button(self)
        self.bttn3['text'] = "/"
        self.bttn3["command"] = self.div_count
        self.bttn3.grid()
        self.bttn3.configure(bg='black')
        self.bttn3.configure(fg='yellow')

        self.bttn4 = Button(self)
        self.bttn4['text'] = "x"
        self.bttn4["command"] = self.mult_count
        self.bttn4.grid()
        self.bttn4.configure(bg='black')
        self.bttn4.configure(fg='green')
    def add_count(self):
        self.lbl_total += 1
        self.lbl["text"] = "Total: " + str(self.lbl_total)
    def sub_count(self):
        self.lbl_total -= 1
        self.lbl["text"] = "Total: " + str(self.lbl_total)
    def div_count(self):
        self.lbl_total //= 2
        self.lbl["text"] = "Total: " + str(self.lbl_total)
    def mult_count(self):
        self.lbl_total *= 50
        self.lbl["text"] = "Total: " + str(self.lbl_total)


root = Tk()
root.title("Click Counter")
root.geometry("200x100")
app = Application(root)

root.mainloop()

from tkinter import *

class Application(Frame):
    "GUI application which counts button clicks"
    def __init__(self, master):
        """Initialize the Frame"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widget()

    def create_widget(self):
        # create instruction label
        self.inst_lbl = Label(self, text = "Enter password for the secret of life")
        self.inst_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)
        #create label for password

        self.pw_ent = Entry(self)
        self.pw_lbl = Label (self, text = "Password: ")
        self.pw_lbl.grid(row = 0, column = 0, sticky = W)

        self.pw_ent.grid(row = 1, column = 1, sticky = W)

        self.submit_bttn = Button(self, text = "Submit", command = self.reveal)
        self.submit_bttn.grid(row = 2, column = 0, sticky = W)

        #create text widget to display message
        self.secret_txt = Text(self, width = 35, height = 5, wrap = WORD)
        self.secret_txt.grid(row= 3, column = 0, columnspan = 2, sticky = W)

    def reveal(self):
        contents = self.pw_ent.get()
        if contents == "secret":
            message = "42"
        else:
            message = "That's not the correct password, so I can not share the the secret with you"
        self.secret_txt.delete(0.0, END)
        self.secret_txt.insert(0.0, message)


root = Tk()
root.title("secret of life")
root.geometry("300x300")
app = Application(root)
root.mainloop()

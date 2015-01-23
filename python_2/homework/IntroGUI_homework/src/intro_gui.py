from tkinter import *
from math import fsum


class Application(Frame):
    """ Application main window class """
    def __init__(self, master=None):
        """ Main frame initialization """
        Frame.__init__(self)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        """ Add all widgets to the main frame """
        top_frame = Frame(self)
        self.label = Label(top_frame, text='Sum of input')
        self.label.pack()
        self.input1 = Entry(top_frame)
        self.input2 = Entry(top_frame)
        self.input1.pack(side=LEFT)
        self.input2.pack(side=RIGHT)
        top_frame.pack(side=TOP)

        bottom_frame = Frame(self)
        bottom_frame.pack(side=TOP)
        self.handleb = Button(bottom_frame, text='Sum', command=self.handle).pack(side=RIGHT)

    def handle(self):
        """ Handle a click of the button by converting the entry
        inputs to floats, and displaying their sum in the label.
        Otherwise, display error text in label. """
        try:
            output = fsum([float(self.input1.get()), float(self.input2.get())])
        except:
            output = "***ERROR***"
        self.label.config(text=output)

root = Tk()
app = Application(master=root)
app.mainloop()

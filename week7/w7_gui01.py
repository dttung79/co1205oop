from tkinter import *

class MyWindow:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("300x50")
        self.window.title("GUI Example")

        self.btn = Button(self.window, text="Click Me", command=self.clicked)
        self.btn.grid(column=0, row=0)

        self.lbl = Label(self.window, text="Hello")
        self.lbl.grid(column=1, row=0)

    def clicked(self):
        self.lbl.configure(text="Button was clicked!")
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    win = MyWindow()
    win.run()
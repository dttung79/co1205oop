from tkinter import *

class ComputerStore:
    def __init__(self):
        self.window = self.create_window()
        self.create_widgets()
    
    def create_window(self):
        window = Tk()
        window.title("Computer Store")
        window.geometry("300x300")
        return window
    
    def create_widgets(self):
        self.lbl_store = Label(self.window, text="Computer Store")
        self.lbl_store.grid(row=0, column=0)

        self.lbl_select = Label(self.window, text="Select a product:")
        self.lbl_select.grid(row=1, column=0, sticky=W)

        self.computer_price = IntVar()
        self.rd_pro13 = Radiobutton(self.window, text="MacBook Pro 13-inch ($2000)", value=2000, 
                                    variable=self.computer_price, command=self.calculate_price)
        self.rd_pro13.grid(row=2, column=0, sticky=W)

        self.air13 = Radiobutton(self.window, text="MacBook Air 13-inch ($1500)", value=1500,
                                    variable=self.computer_price, command=self.calculate_price)
        self.air13.grid(row=3, column=0, sticky=W)

        self.pro15 = Radiobutton(self.window, text="MacBook Pro 15-inch ($2500)", value=2500,
                                    variable=self.computer_price, command=self.calculate_price)
        self.pro15.grid(row=4, column=0, sticky=W)

        self.lbl_option = Label(self.window, text="Select an option:")
        self.lbl_option.grid(row=5, column=0, sticky=W)

        self.cover_var = BooleanVar()
        self.chk_cover = Checkbutton(self.window, text="Cover ($10)", variable=self.cover_var,
                                        command=self.calculate_price)
        self.chk_cover.grid(row=6, column=0, sticky=W)

        self.case_var = BooleanVar()
        self.chk_case = Checkbutton(self.window, text="Case ($20)", variable=self.case_var,
                                        command=self.calculate_price)
        self.chk_case.grid(row=7, column=0, sticky=W)

        self.lbl_price = Label(self.window, text="Total Price:")
        self.lbl_price.grid(row=8, column=0, sticky=W)

        self.total_price = IntVar()
        self.txt_price = Entry(self.window, width=20, state="readonly", 
                                textvariable=self.total_price)
        self.txt_price.grid(row=9, column=0, sticky=W)

    def calculate_price(self):
        price = self.computer_price.get() # get selected computer price
        if self.cover_var.get():    # if user selects cover
            price += 10
        
        if self.case_var.get():     # if user selects case
            price += 20
        
        self.total_price.set(price) # set total price to the Entry widget

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = ComputerStore()
    app.run()
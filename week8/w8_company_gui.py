from tkinter import *
from tkinter import messagebox as msb
from tkinter import filedialog
import csv
from w8_employee import Employee

class CompanyGUI:
    def __init__(self):
        self.create_window()
        self.create_widgets()
        self.__employees = []
    
    def create_window(self):
        self.window = Tk()
        self.window.title("FPT Company")
        self.window.geometry("500x350")
    
    def create_widgets(self):
        self.lbl_company = Label(self.window, text="FPT Company Employees")
        self.lbl_company.grid(row=0, column=0, columnspan=6)

        self.create_listbox()
        self.create_info_widgets()
        self.create_navigation_buttons()

    def create_listbox(self):
        self.btn_load = Button(self.window, text="Load", command=self.load_employees)
        self.btn_load.grid(row=1, column=0, sticky=W, padx=5, pady=5)

        # selectmode: choose 1 item only
        # exportselection: keep item selected even when listbox loses focus
        self.lst_employees = Listbox(self.window, width=20, height=10, 
                                        selectmode=SINGLE, exportselection=False)
        self.lst_employees.grid(row=2, column=0, rowspan=4, padx=5, pady=5)
        self.lst_employees.bind("<<ListboxSelect>>", self.show_employee_info)
    
    def show_employee_info(self, event):
        selected_index = self.lst_employees.curselection()[0]
        selected_employee = self.__employees[selected_index]
        self.update_entry(self.txt_id, selected_employee.id)
        self.update_entry(self.txt_name, selected_employee.name)
        self.update_entry(self.txt_rate, selected_employee.rate)
    
    def update_entry(self, entry, value):
        entry.delete(0, END)
        entry.insert(0, value)


    def load_employees(self):
        file_name = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), 
                                                            ("All files", "*.*")])
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                id = int(row[0])
                name = row[1]
                rate = float(row[2])
                self.__employees.append(Employee(id, name, rate))
                self.lst_employees.insert(END, name)
        
        # set the first employee as the default selected item
        self.lst_employees.select_set(0)
        self.show_employee_info(None)
    
    def create_info_widgets(self):
        self.lbl_search = Label(self.window, text="Search")
        self.lbl_search.grid(row=1, column=1, sticky=E, padx=5, pady=5)

        self.txt_search = Entry(self.window, width=25)
        self.txt_search.grid(row=1, column=2, padx=5, pady=5, columnspan=4, sticky=W)
        self.txt_search.bind("<Return>", self.search_employees)

        self.lbl_id = Label(self.window, text="ID")
        self.lbl_id.grid(row=2, column=1, sticky=E+N, padx=5, pady=5)

        self.txt_id = Entry(self.window, width=25)
        self.txt_id.grid(row=2, column=2, padx=5, pady=5, columnspan=4, sticky=W+N)

        self.lbl_name = Label(self.window, text="Name")
        self.lbl_name.grid(row=3, column=1, sticky=E+N, padx=5, pady=5)

        self.txt_name = Entry(self.window, width=25)
        self.txt_name.grid(row=3, column=2, padx=5, pady=5, columnspan=4, sticky=W+N)

        self.lbl_rate = Label(self.window, text="Rate")
        self.lbl_rate.grid(row=4, column=1, sticky=E+N, padx=5, pady=5)

        self.txt_rate = Entry(self.window, width=25)
        self.txt_rate.grid(row=4, column=2, padx=5, pady=5, columnspan=4, sticky=W+N)

    def create_navigation_buttons(self):
        self.btn_first = Button(self.window, text="|<", command=self.move_first)
        self.btn_first.grid(row=5, column=2, padx=5, pady=5)

        self.btn_previous = Button(self.window, text="<<", command=self.move_previous)
        self.btn_previous.grid(row=5, column=3, padx=5, pady=5)

        self.btn_next = Button(self.window, text=">>", command=self.move_next)
        self.btn_next.grid(row=5, column=4, padx=5, pady=5)

        self.btn_last = Button(self.window, text=">|", command=self.move_last)
        self.btn_last.grid(row=5, column=5, padx=5, pady=5)

        self.btn_exit = Button(self.window, text="Exit", command=self.window.quit)
        self.btn_exit.grid(row=6, column=5, padx=5, pady=5, sticky=E)
    
    def move_first(self):
        # clear selection
        self.lst_employees.selection_clear(0, END)
        # select the first item
        self.lst_employees.select_set(0)
        self.show_employee_info(None)

    def move_previous(self):        
        selected_index = self.lst_employees.curselection()[0]
        if selected_index == 0:
            msb.showinfo("Information", "This is the first employee")
        else:
            # clear selection
            self.lst_employees.selection_clear(0, END)
            # select the previous item
            self.lst_employees.select_set(selected_index - 1)
            self.show_employee_info(None)

    def move_next(self):
        pass

    def move_last(self):
        pass

    def search_employees(self, event):
        name = self.txt_search.get()
        found = False
        for i in range(len(self.__employees)):
            if name.lower() in self.__employees[i].name.lower():
                self.lst_employees.selection_clear(0, END)
                self.lst_employees.select_set(i)
                self.show_employee_info(None)
                msb.showinfo("Information", "Employee found")
                found = True
                break
        if not found:
            msb.showinfo("Information", "Employee not found")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    company = CompanyGUI()
    company.run()
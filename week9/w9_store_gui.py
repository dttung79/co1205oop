from w9_base_gui import BaseGUI
from tkinter import *
from tkinter import messagebox as msb
import csv
from tkinter import filedialog

from w9_item import Item

class StoreGUI(BaseGUI):
    def __init__(self):
        super().__init__("Item Store", "450x350")
        self.__items = []
    
    def _create_widgets(self):
        self.__create_listbox()
        self.__create_textboxes()
        self.__create_buttons()

    def __create_listbox(self):
        self.__lst_items = Listbox(self._window, width=20, height=10, 
                                    selectmode=SINGLE, exportselection=0)
        self.__lst_items.grid(row=0, column=0, rowspan=4, columnspan=2, padx=5, pady=5, sticky=W)
        self.__lst_items.bind("<<ListboxSelect>>", self.__on_select)

    def __on_select(self, event):
        # get selected index
        selected_index = self.__lst_items.curselection()[0]
        item = self.__items[selected_index]
        self.__update_textbox(self.__txt_id, item.item_id)
        self.__update_textbox(self.__txt_name, item.name)
        self.__update_textbox(self.__txt_brand, item.brand)
        self.__update_textbox(self.__txt_price, item.price)
    
    def __update_textbox(self, textbox, value):
        textbox.delete(0, END)
        textbox.insert(0, value)

    def __create_textboxes(self):
        lbl_id = Label(self._window, text="ID:")
        lbl_id.grid(row=0, column=2, padx=5, pady=5, sticky=E)
        self.__txt_id = Entry(self._window)
        self.__txt_id.grid(row=0, column=3, padx=5, pady=5, sticky=W, columnspan=3)

        lbl_name = Label(self._window, text="Name:")
        lbl_name.grid(row=1, column=2, padx=5, pady=5, sticky=E)
        self.__txt_name = Entry(self._window)
        self.__txt_name.grid(row=1, column=3, padx=5, pady=5, sticky=W, columnspan=3)

        lbl_brand = Label(self._window, text="Brand:")
        lbl_brand.grid(row=2, column=2, padx=5, pady=5, sticky=E)
        self.__txt_brand = Entry(self._window)
        self.__txt_brand.grid(row=2, column=3, padx=5, pady=5, sticky=W, columnspan=3)

        lbl_price = Label(self._window, text="Price:")
        lbl_price.grid(row=3, column=2, padx=5, pady=5, sticky=E)
        self.__txt_price = Entry(self._window)
        self.__txt_price.grid(row=3, column=3, padx=5, pady=5, sticky=W, columnspan=3)

    def __create_buttons(self):
        btn_add = Button(self._window, text="Add", command=self.__add_item)
        btn_add.grid(row=4, column=3, padx=5, pady=5, sticky=W)

        btn_edit = Button(self._window, text="Edit", command=self.__edit_item)
        btn_edit.grid(row=4, column=4, padx=5, pady=5, sticky=W)

        btn_delete = Button(self._window, text="Delete", command=self.__delete_item)
        btn_delete.grid(row=4, column=5, padx=5, pady=5, sticky=W)

        btn_load = Button(self._window, text="Load", command=self.__load_items)
        btn_load.grid(row=4, column=0, padx=5, pady=5, sticky=W)

        btn_save = Button(self._window, text="Save", command=self.__save_items)
        btn_save.grid(row=4, column=1, padx=5, pady=5, sticky=E)

    def __add_item(self):
        # get item info from the textboxes
        item_id = int(self.__txt_id.get())
        name = self.__txt_name.get()
        brand = self.__txt_brand.get()
        price = float(self.__txt_price.get())
        # create Item object
        item = Item(item_id, name, brand, price)
        # add the item to the list
        self.__items.append(item)
        # add the item name to the listbox
        self.__lst_items.insert(END, name)

        msb.showinfo("Item Added", f"Item {name} added successfully.")

    def __edit_item(self):
        # get item info from the textboxes
        name = self.__txt_name.get()
        brand = self.__txt_brand.get()
        price = float(self.__txt_price.get()) 
        # get selected index & selected item
        selected_index = self.__lst_items.curselection()[0]
        item = self.__items[selected_index]
        # update item info
        item.name = name
        item.brand = brand
        item.price = price
        # update listbox
        self.__lst_items.delete(selected_index)
        self.__lst_items.insert(selected_index, name)

        msb.showinfo("Item Updated", f"Item {name} updated successfully.")

    def __delete_item(self):
        # get selected index
        selected_index = self.__lst_items.curselection()[0]
        # remove the item at index
        item = self.__items.pop(selected_index)
        # remove the item from the listbox
        self.__lst_items.delete(selected_index)

        msb.showinfo("Item Deleted", f"Item {item.name} deleted successfully")

    def __load_items(self):
        file_name = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), 
                                                            ("All files", "*.*")])
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            next(reader)        # skip the header
            for row in reader:
                # read item info from the file
                item_id = int(row[0])
                name = row[1]
                brand = row[2]
                price = float(row[3])
                item = Item(item_id, name, brand, price)
                self.__items.append(item)           # add the item to the list
                self.__lst_items.insert(END, name)  # add the item name to the listbox
        
        msb.showinfo("Items Loaded", f"{len(self.__items)} items loaded successfully.")

    def __save_items(self):
        # open a file to save
        file_name = filedialog.asksaveasfilename(filetypes=[("CSV files", "*.csv"), 
                                                            ("All files", "*.*")])
        with open(file_name, "w", newline="\n") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Item Name", "Brand", "Price"])
            for item in self.__items:
                writer.writerow([item.item_id, item.name, item.brand, item.price])

        msb.showinfo("Items Saved", f"{len(self.__items)} items saved successfully.")
        
if __name__ == "__main__":
    app = StoreGUI()
    app.run()
import tkinter as tk

class Interface:
    def __init__(self):
        self.root = tk.Tk()

        self.listbox = tk.Listbox(self.root)
        self.listbox.insert(1, "Choice 1")
        self.listbox.insert(2, "Choice 2")
        self.listbox.insert(3, "Choice 3")
        self.listbox.bind('<<ListboxSelect>>', self.update_entries)
        self.listbox.pack()

        self.entry1 = tk.Entry(self.root)
        self.entry1.pack()
        self.entry2 = tk.Entry(self.root)
        self.entry2.pack()
        self.entry3 = tk.Entry(self.root)
        self.entry3.pack()
        self.entry4 = tk.Entry(self.root)
        self.entry4.pack()
        self.entry5 = tk.Entry(self.root)
        self.entry5.pack()

    def update_entries(self, event):
        selection = self.listbox.get(self.listbox.curselection())  # get the selected item from listbox
        self.entry1.delete(0, tk.END)  # clear previous content from entry widgets
        self.entry2.delete(0, tk.END)
        self.entry3.delete(0, tk.END)
        self.entry4.delete(0, tk.END)
        self.entry5.delete(0, tk.END)
        # update the entries based on the selected item from listbox
        self.entry1.insert(0, selection)
        self.entry2.insert(0, selection + "_entry2")
        self.entry3.insert(0, selection + "_entry3")
        self.entry4.insert(0, selection + "_entry4")
        self.entry5.insert(0, selection + "_entry5")

    def run(self):
        self.root.mainloop()

interface = Interface()
interface.run()

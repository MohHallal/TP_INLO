from tkinter import *

class Application(Tk):
    def __init__(self, controller):
        Tk.__init__(self)
        self.controller = controller
        self.attributes = self.controller.get_model_entries()
        self.animals = self.controller.get_model_animals()
        self.creer_widgets()

    def creer_widgets(self):
        """Une méthode qui crée la fenetre"""
        self.label = Label(self, text="J'adore Python !")
        self.label1 = Label(self, text="")
        self.label_search = Label(self, text="Recherche:")
        self.bouton_display = Button(self, text="Afficher", command=self.display_something)
        self.bouton = Button(self, text="Quitter", command=self.quit_window)
        self.add = Label(self, text="Add:")
        self.bouton_add_animal = Button(self, text="Add", command=self.add_animal)
        self.listbox=Listbox(self,exportselection=False)
        i = 1
        for animal in self.animals:
            self.listbox.insert(i,animal)
            i += 1
        self.delete = Label(self, text="Delete:")
        self.bouton_delete = Button(self, text="Delete", command=self.delete_animal)
        self.search = Entry(self)
        self.entries = {}
        self.entries_label = {}
        for att in self.attributes:
            self.entries[att] = Entry(self)
            self.entries_label[att] = Label(self, text=att)
        self.listbox_modify=Listbox(self,exportselection=False)
        self.label_modify_seperator = Label(self, text="The new informations")
        self.label_modify_seperator2 = Label(self, text="____________________")
        self.label_modify_seperator3 = Label(self, text="The animal to modify:")
        i = 1
        for animal in self.animals:
            self.listbox_modify.insert(i,animal)
            i += 1
        self.modify = Label(self, text="Modify:")
        self.entries_modify = {}
        self.entries_label_modify = {}
        for att in self.attributes:
            self.entries_modify[att] = Entry(self)
            self.entries_label_modify[att] = Label(self, text=att)
        self.listbox_modify.bind('<<ListboxSelect>>', self.update_entries)
        self.bouton_modify = Button(self, text="Modify", command=self.modify_animal)
        self.label.pack()
        self.label1.pack()
        self.label_search.pack()
        self.search.pack()
        self.bouton_display.pack()
        self.delete.pack()
        self.listbox.pack()
        self.bouton_delete.pack()
        self.modify.pack()
        self.label_modify_seperator3.pack()
        self.listbox_modify.pack()
        self.label_modify_seperator.pack()
        self.label_modify_seperator2.pack()
        for att in self.attributes:
            self.entries_label_modify[att].pack()
            self.entries_modify[att].pack()
        self.bouton_modify.pack()
        self.add.pack()
        for att in self.attributes:
            self.entries_label[att].pack()
            self.entries[att].pack()
        self.bouton_add_animal.pack()
        self.bouton.pack()
    def quit_window(self):
        """Une méthode qui ferme la fenetre"""
        self.controller.quit_window()

    def display_something(self):
        """Une méthode qui cherche un animal"""
        self.controller.display(self.search.get())

    def display_label(self, value):
        self.label1['text'] = value

    def add_animal(self):
        dict_animal = {}
        for key in self.entries:
            dict_animal[key] = self.entries[key].get()
        self.controller.add_animal(dict_animal)
        for key in self.entries:
            self.entries[key].delete(0,END)
        self.open_popup()

    def delete_animal(self):
        for i in self.listbox.curselection():
            self.controller.delete_animal(self.listbox.get(i))
    def update_entries(self,_):
        for att in self.attributes:
            self.entries_modify[att].delete(0,END)
        nbr_entries = len(self.attributes)
        for i in self.listbox_modify.curselection():
            updates = self.controller.default_values(self.listbox.get(i))
            for i in range(0, nbr_entries):
                self.entries_modify[self.attributes[i]].insert(0, updates[i])

    def modify_animal(self):
        the_update = ""
        for key in self.entries_modify:
            the_update = the_update + str(self.entries_modify[key].get()) + ","
        the_update=the_update[:-1]+"\n"
        for i in self.listbox_modify.curselection():
            self.controller.modify_animal(self.listbox.get(i),the_update)
        for key in self.entries_modify:
            self.entries_modify[key].delete(0,END)
    def view_window(self):
        self.title("Ma Première App :-)")
        self.mainloop()
    def open_popup(self):
       self.top= Toplevel(self)
       self.top.geometry("750x250")
       self.top.title("Pop-up")
       Label(self.top, text= "Animal sauvé avec succés!", font=('Mistral 18 bold')).place(x=150,y=80)

if __name__ == "__main__":
    app = Application()
    app.view_window()
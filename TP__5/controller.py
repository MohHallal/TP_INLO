from vue import Application
from model import Model

class Controller() :
    def __init__(self):

        self.model = Model("a.txt")
        self.model.read_file()
        self.view = Application(self)
        self.view.view_window()

    def display(self, value):
        self.view.display_label(self.model.dico_animaux[value])

    def add_animal(self, dict_animal):
        self.model.save(dict_animal)
    def delete_animal(self, animal):
        self.model.delete(animal)
    def modify_animal(self,name,new_information):
        self.model.modify_animal(name,new_information)
    def get_model_entries(self):
        return self.model.get_attributes()

    def get_model_animals(self):
        return self.model.animals_names
    def default_values(self,value):
        return self.model.default_values(value)

    def quit_window(self):
        print("close app")
        self.model.close()
        self.view.destroy()

if __name__ == "__main__" :
    C = Controller()
""" Application est la classe qui crée l'interface"""
from vue import Application
from model import Model

class Controller() :
    """ Classe qui contient les méthodes su controlleur"""
    def __init__(self):

        self.model = Model("a.txt")
        self.model.read_file()
        self.view = Application(self)
        self.view.view_window()

    def display(self, value):
        """ Une méthode qui raméne les données d'un animal"""
        self.view.display_label(self.model.dico_animaux[value])

    def add_animal(self, dict_animal):
        """ Une méthode qui ajoute un animal"""
        self.model.save(dict_animal)
    def delete_animal(self, animal):
        """ Une méthode qui supprime un animal"""
        self.model.delete(animal)
    def modify_animal(self,name,new_information):
        """ Une méthode qui modifie un animal"""
        self.model.modify_animal(name,new_information)
    def get_model_entries(self):
        """ Une méthode qui raméne les clés"""
        return self.model.get_attributes()

    def get_model_animals(self):
        """ Une méthode qui raméne les noms des animaux"""
        return self.model.animals_names
    def default_values(self,value):
        """ Une méthode qui raméne les données d'un animal /
        pour les mettre par défault dans les entries"""
        return self.model.default_values(value)

    def quit_window(self):
        """Une méthode qui fait la fermeture de l'interface"""
        print("close app")
        self.model.close()
        self.view.destroy()

if __name__ == "__main__" :
    C = Controller()

"""hhhhhh"""
import os
from animal import Animal
class Model():
    """This class manipulates the animal class files"""
    def __init__(self, filename):
        self.filename = filename
        self.file=open(self.filename, "r+",encoding="utf-8")
        self.dico_animaux = {}
        self.animals_names = []
    def read_file(self):
        """Cette methode fait la lecture des fichiers"""
        for line in self.file:
            line = line.strip()
            tab = line.split(",")
            animal_data = Animal(tab[0],tab[1],tab[2],tab[3],tab[4])
            self.dico_animaux[animal_data.name] = animal_data
            self.animals_names.append(animal_data.name)
    def save(self, dict_animal):
        """Cette méthode ajoute un animal"""
        self.file.write("\n"+dict_animal["species"]+","+dict_animal["age"]
                        +","+dict_animal["diet"]+","+dict_animal["foot"]
                        +","+dict_animal["name"])

    def delete(self, animal):
        """Cette méthode supprime un animal"""
        self.file.seek(0)
        with open("temporary.txt","w",encoding="utf-8") as temp:
            for line in self.file:
                if str(animal) not in line:
                    temp.write(line)
        os.replace("temporary.txt",self.filename)

    def modify_animal(self,name,new_informations):
        """Cette méthode modifie un animal"""
        self.file.seek(0)
        with open("temporary.txt","w",encoding="utf-8") as temp:
            for line in self.file:
                if str(name) in line:
                    temp.write(new_informations)
                else:
                    temp.write(line)
        os.replace("temporary.txt", self.filename)

    def default_values(self,value):
        """Cette méthode récupére la ligne correspond a un name d'animal"""
        self.file.seek(0)
        for line in self.file:
            if str(value) in line:
                line = line.strip().split(",")
                return line

    def close(self):
        """Cette methode ferme la fenetre"""
        self.file.close()

    def get_attributes(self)->[]:
        """Cette methode return les attributs"""
        attr = []
        # get first key of the dict no mater what is it
        first_key = next(iter(self.dico_animaux))
        for key in self.dico_animaux[first_key].__dict__:
            attr.append(key)
        return attr

if __name__ == "__main__" :
    model = Model("a.txt")
    model.read_file()
    model.close()

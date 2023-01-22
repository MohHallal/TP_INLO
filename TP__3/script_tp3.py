# encoding : utf8
import gc
class Arbre():
    def __init__(self, mother, children) -> None:
        self.mother = mother
        self.children = children
        self.ancestors=[] # ancestors will have a list containing mother, grandmother, grand grandmother ... (if exists)
        ancestor=find_mother(mother) # find_mother is a function defined blow, its role is to bring the mother of a given child if exists, and returns None if there isn't
        while ancestor!=None: # retrieve mother of mother of mother ... until there is no more.
            self.ancestors.append(ancestor)
            ancestor=find_mother(ancestor)
    def set_mother(self, mother):
        self.mother = mother
    def add_children(self,child) -> None:
        if child not in self.children:
            self.children.append(child)
        else:
            pass
    def remove_children(self,child) -> None:
        if child in self.children:
            self.children.remove(child)
        else:
            pass
    def descendance(self): # This function returns the first and the second generation of a given mother
        if self.children: # Check the existence of children for the mother
            generation1=self.children
            generation2=""
            for child in generation1: # The next bloc collects the children of all the children of the mother in the variable Generation2
                for family in gc.get_objects(): # Iterates all the variables of the script
                    if isinstance(family, Arbre): # Check each variable if it is an instance of the class Arbre
                        if child in family.mother: # Check if the child is a mother of a family
                            generation2=generation2+ ", ".join(family.children) # Add the founded children to generation2
                            generation2 = generation2 + ", "
        else:
            return self.mother + " n'a pas d'enfants."
        return self.mother + "\n Generation 1: " + ", ".join(generation1) + "\n Generation 2: " + generation2
    def __str__(self) -> str:
        return "Mother: " + self.mother + ".\nChildren: " + ", ".join(self.children) + "."
    def __eq__(self, __o: object) -> bool:
        return self.mother == __o.mother and self.children == __o.children
def find_mother(child): # This function returns the mother of a given child if exists, and None if it doesn't
    for family in gc.get_objects(): # Iterates all the variables of the script
        if isinstance(family, Arbre): # Check each variable if it is an instance of the class Arbre
            if child in family.children: # Check if the child is one of children of a family
                return family.mother
    return None

if __name__ == "__main__":
    family1=Arbre("Chat",["Chat1","Chat2","Chat3"])
    family2=Arbre("Chat1",["Chat4","Chat5","Chat6"])
    family3=Arbre("Chat4",["Chat7","Chat8","Chat9"])
    family3.add_children("Chat10")
    family3.remove_children("Chat8")

    print(family3.ancestors)

    print(find_mother("Chat4"))
    print(find_mother("Chat7"))

    print(family1.descendance())
    print(family2.descendance())

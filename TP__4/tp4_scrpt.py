"""This method prints trees"""
class Binary():
    """This class organizes trees"""
    def __init__(self):
        self.root=None
    def print_tree(self,position,position_alternatif = None):
        """This method prints trees"""
        retour=""
        for _ in range(0, position):
            retour+="\t"
        retour+=str(self.root.value)+ "/" + str(self.root.depth)
        if position_alternatif:
            position=position_alternatif
        if self.root.left:
            retour += "\n"
            tree = Binary()
            tree.root = self.root.left
            retour+= tree.print_tree(position-1)
        if self.root.right:
            tree = Binary()
            tree.root = self.root.right
            if self.root.left: # position_alternatif considére ce cas
                retour += tree.print_tree(2,position)
            else:
                retour += "\n"
                retour += tree.print_tree(position+2)
        return retour
    def tree_size(self,node):
        """ This method returns the number of nodes """
        tree=Binary()
        tree.root=node
        count_lefts = 0
        count_rights = 0
        if node.left:
            tree = Binary()
            tree.root = node.left
            count_lefts = 1 + tree.tree_size(node.left)
        if node.right:
            tree = Binary()
            tree.root = node.right
            if node.left:
                count_rights=tree.tree_size(node.right)
            else: # if we don't add this bloc, the node that have a left and a right child will be counted twice
                count_rights= 1 + tree.tree_size(node.right)
        if node.is_leaf():
            return 1
        return count_lefts + count_rights
class Node():
    def __init__(self, value):
        self.value=value
        self.right= None
        self.left= None
        self.depth= 0
    def add(self, right = None, left = None):
        self.left = left
        self.right = right
        if self.left:
            left.depth = self.depth + 1
            left.update_children_depth()
        if self.right:
            right.depth = self.depth + 1
            right.update_children_depth()
    def update_children_depth(self):
        if self.left:
            self.left.depth = self.depth + 1
            self.left.update_children_depth()
        if self.right:
            self.right.depth = self.depth + 1
            self.right.update_children_depth()
    def display_node(self):
        retour = str(self)
        if self.right:
            retour += " " + self.right.display_node()
        if self.left:
            retour += " " + self.left.display_node()

        return retour
    def __str__(self):
        return str(self.value) + "/" + str(self.depth)
    def is_leaf(self):
        #return self.left == None and self.right == None
        return not(self.left or self.right)
    def get_max_depth(self,max_depth=0):
        if self.is_leaf():
            if self.depth > max_depth:
                return self.depth
            else:
                return max_depth
        # je suis le node d'un arbre
        else:
            if self.right:
                max_depth = self.right.get_max_depth(max_depth)

            if self.left:
                max_depth = self.left.get_max_depth(max_depth)
            return max_depth
node1 = Node(0)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node3.add(node4)
node1.add(node3, node2)
tree1=Binary()
tree1.root=node1
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node5.add(node7, node6)
node4.add(node5)
node8 = Node(8)
#node7.add(node8)
node7.add(Node(8))
#tree1.root=node1
#print(str(node1.get_max_depth(0)))
#print(node1.display_node())
print(tree1.print_tree(1))
print(tree1.tree_size(node1))

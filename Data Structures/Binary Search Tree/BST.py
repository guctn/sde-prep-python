class Node:
    def __init__ (self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    # it's not necessary to create a BSF or other Data Strucuture with a node 
    # - it can be none and then we insert later the first node
    def __init__ (self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            elif new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contain (self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    
    # def contain (self, value):
    #     if self.root is None:
    #         return False
    #     temp = self.root
    #     while (True):
    #         if value == temp.value:
    #             return True
    #         elif value < temp.value:
    #             if temp.left is None:
    #                 return False
    #             temp = temp.left
    #         else:
    #             if temp.right is None:
    #                 return False
    #             temp = temp.right


        
my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)
print(my_tree.contain(7))
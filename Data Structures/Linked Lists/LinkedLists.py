class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    # every method of the class LinkedList will need to create a new node
    # so it's smarter to create another class just to do it instead of doing 
    # the same thing for each method

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    # The constructor initializes the linked list with a single node. 
    # Both head and tail point to this first node because it’s the only 
    # element in the list. The length is set to 1.
    
    def print_list(self):
        values = []
        temp = self.head
        while temp is not None:
            values.append(str(temp.value))
            temp = temp.next
        values.append("None")
        print(" -> ".join(values))
    # it just prints each value of a linked list until if finds a none node

    # Big O(1) -> because it needs to just update the tail.next and the tail
    # first create a new node
    # check if there are any values first
    # then update tail.next = new and tail = new
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node 
        # it checks if the linked list is empty
        else:
            self.tail.next = new_node # sets the tail next value first
            self.tail = new_node      # sets the tail to the last value
        self.length += 1
        return True

    #big O(n) -> because it needs to go all through the linked list
    # first check if the LL is empty (None)
    # second check if there is only one node (update everything to None)
    # third - iterate through the list until you find the last node (tail.next = None)
    # and store the previous last node position then update tail to prev
    # and tail.next to None
    def pop(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            temp = self.tail
            self.head = None
            self.tail = None
        else:
            pre = self.head
            temp = self.head
            while temp.next:    #while temp.next is True, if temp.next = None then is false
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
        self.length -= 1
        return temp

    #Big O(1) -> because we only need to change the head 
    # first create a new node
    # then check if the LL is None (empty) then update head and tail to point to new node
    # later, the new node next is going to be the first node (head) 
    # and then update head to point to the new node
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    #Big O(1) -> because we'll only change the head and the size of the list doesn't matter
    # first check if the LL is empty (if True return None)
    # second check if there's only one node - then set everything to None
    # third update head to be head.next and the temp (first value) to temp.next equals None
    def pop_first(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
        self.length -= 1
        return temp
    
    # Big O(n)
    # first is necessary to check if the index is valid
    # so check if it's less than 0 or greater or equal do length then return none
    # later just go through the LL index times (so if 2, for runs 2 times)
    # and update temp to the next node
    def get (self, index):
        if index < 0 or index >= self.length: # se o index for maior que o lenght - quer dizer que não tem nodes nesse index
            return None                       # se o indx é igual ao length também não da porque o index sempre começa no 0 ou seja é maior que a LL
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    # Big O(n)
    # we'll receive the postion to be changed and the new value - 
    # first we need to find the object of chosen index - so we use get()
    # if the index is not valid get() will return None and we can't change the object value to None
    # so if we receive None then we return False
    # if it's not None we update the node value
    def set_value(self, index, value):
        temp = self.get(index)
        if temp is not None: # pode return None se o index for menor que 0 ou maior e igual que a length
            temp.value = value
            return True
        return False
    
    #Big O(n)
    def insert(self, index, value):
        if index < 0 or index > self.length: # index out of range
            return False
        elif index == 0:                    # adding in the beginning
            return self.prepend(value)
        elif index == self.length:        # adding in the end
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove (self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == (self.length-1):
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    def reverse (self):
        if self.length is None or self.length == 1:
            return False
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        while temp:
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return True

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.print_list()

print(my_linked_list.reverse())
my_linked_list.print_list()








#print(my_linked_list.head.value)
# Here we access the value of the head node directly with 
# my_linked_list.head.value. If the list had more nodes, 
# we would need to follow the next pointers to reach them.





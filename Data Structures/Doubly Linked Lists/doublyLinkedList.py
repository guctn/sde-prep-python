# Doubly Linked Lists are the same of Singly Linked Lists. The only different is that
# we can track the previous node and next node - making things like pop/insert/remove easir
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedLists:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        values = ["None"]
        temp = self.head
        while temp is not None:
            values.append(str(temp.value))
            temp = temp.next
        values.append("None")
        print(" <-> ".join(values))

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else: 
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            temp.next = None
            self.head.prev = None
        self.length -= 1
        return temp 

    def get (self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < (self.length // 2):
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1,index, -1): # starts at length minus 1, ends in index, and increments by minus 1
                temp = temp.prev    # length - 1 -> gets the last index and then goes backwards until the index
        return temp
    
    def set_value (self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        elif index == self.length:
            return self.append(value)
        elif index == 0:
            return self.prepend(value)
        else:
            new_node = Node(value)
            after = self.get(index)
            before = after.prev
            new_node.next = after
            new_node.prev = before
            after.prev = new_node
            before.next = new_node
        self.length += 1
        return True

    def remove (self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        temp = self.get(index)
        after = temp.next
        before = temp.prev
        before.next = after
        after.prev = before 
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp
    
    # other way to write 
    # temp = self.get(index)
    # temp.next.prev = temp.prev
    # temp.prev.next = temp.next
    # temp.next = None
    # temp.prev = None




my_doubly_linked_list = DoublyLinkedLists(1)
my_doubly_linked_list.append(3)
my_doubly_linked_list.print_list()

my_doubly_linked_list.remove(1)
print(my_doubly_linked_list.remove(1))

my_doubly_linked_list.print_list()

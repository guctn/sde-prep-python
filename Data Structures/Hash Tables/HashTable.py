class HashTable:
    def __init__ (self, size = 7): #this is a default size - if someone gives a number for size it'll no be 7
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    # ord -> ordinal = it gets the Ascii number for each letter
    # it sums with the previous my_hash but before it 
    # multiplies by 23 - which is a prime number (it could be any prime number)
    # module operator -> gets the remainder when divided
    # then if you divide any number by seven (list's length), the remainder 
    # will be always in range of 0 to 6 (the list addresses)
    # return my_hash -> this'll be the address we'll place the key value pair

    def set_item(self, key, value):
        # it's going to use the hash method on the to create the address
        # and it's algo going to create the key value pair in a list
        # however when it goes to the hash table addres it's going to get in another list
        # it'll look like this 4 = [ ['bolts', 1400] ]
        index = self.__hash(key)
        # here we're discovering which address our key value pair will go
        if self.data_map[index] == None:
            # we have a IF because we'll only create the list in the address if it doesn't have already
            self.data_map[index] = []
            # here we're adding a empty list in the addres we receive from hash method
        self.data_map[index].append([key, value])
        # here we're addind the key value pair in a list in the addres

    def get_item(self, key):
        index = self.__hash(key)
        value = self.data_map[index]
        if value is not None:
            for item in value:
                if item[0]== key:
                    return item[1]
        return None

    # def get_item(self, key):
    #     index = self.__hash(key)
    #     if self.data_map[index] is not None:
    #         for i in range(len(self.data_map[index])):
    #             if self.data_map[index][i][0] == key:
    #                 return self.data_map[index][i][1]
    #     return None

    def keys_list (self):
        keys = []
        for index in self.data_map:
            if index:
                for item in index:
                    keys.append(item[0])

        return keys

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)


my_hash_table = HashTable()
my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)
my_hash_table.set_item('cool', 8)
my_hash_table.print_table()
print(my_hash_table.get_item('cool'))
print(my_hash_table.keys_list())


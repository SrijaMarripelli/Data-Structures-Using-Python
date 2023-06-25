class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        # Adds a new node to the end of the doubly linked list
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def prepend(self, data):
        # adds a ne w node to the beginning of the doubly linked list
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def remove(self, key):
        # removes a node with the given key from the doubly linked list
        if self.head.data == key:
            self.head = self.head.next
            self.head.prev = None
        else:
            current = self.head
            while current.next:
                if current.data == key:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    return 
                current = current.next
            if current.data == key:
                current.prev.next = None

    def print_list(self):
        # prints all the elements of the doubly linked list
        current = self.head
        while current:
            print(current.data)
            current = current.next

# create a new doubly linked list
dllist = DoublyLinkedList()

# add nodes to the lsit
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4) 
dllist.prepend(5)

# print the list
dllist.print_list()

# remove a node from the list
dllist.remove(2)

# print the updated list
dllist.print_list()


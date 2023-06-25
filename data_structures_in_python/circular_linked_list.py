class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
    
class CircularLinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next - self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            self.head = new_node

    def remove(self, key):
        if self.head.data == key:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
        else:
            current = self.head
            prev = None
            while current.next != self.head:
                prev = current
                current = current.next
                if current.data == key:
                    prev.next = current.next
                    current = current.next

    def print_list(self):
        current = self.head
        while current :
            print(current.data)
            current = current.next
            if current == self.head:
                break

#create a new circular linked list
cllist = CircularLinkedList()

#add nodes to the list
cllist.append(1)
cllist.append(2)
cllist.append(3)
cllist.prepend(4)

#print the list
cllist.print_list()

#remove a node from the list
cllist.remove(2)

#print the updated list
cllist.print_list()
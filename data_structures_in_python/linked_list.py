class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return 
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if self.head is None:
            return 
        if self.head.data == data:
            self.head = self.head.next
            return
        current_node = self.head
        while current_node.next is not None:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

    def display(self):
        current_node = self.head
        while current_node.next is not None:
            print(current_node.data,end=" -> ")
            current_node = current_node.next
        print("None")

linked_list = LinkedList()

linked_list.append(1)
linked_list.display()

linked_list.append(2)
linked_list.display()

linked_list.append(3)
linked_list.display()

linked_list.prepend(4)
linked_list.display()

linked_list.delete(2)
linked_list.display()
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
            self.tail.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
    
    def display(self):
        current = self.head
        if self.head is not None:
            while True:
                print(current.data, end = " -> ")
                current = current.next
                if current == self.head:
                    break
            print("(head)")
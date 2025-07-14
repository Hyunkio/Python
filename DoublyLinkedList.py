class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.head = None
        
    def append(self, data):
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            
    def remove_list(self):
        if not self.tail: #리스트가 비어있는 경우
            raise IndexError("List is empty")
        elif self.head == self.tail: #노드가 1개 있는 경우
            self.head = None
            self.tail = None
        else: #노드 2개 이상 있는 경우
            self.tail = self.tail.prev
            self.tail.next = None
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end = " <-> ")
            current = current.next
        print("None")
        
dlist = DoublyLinkedList()
dlist.append(10)
dlist.append(20)
dlist.append(30)
dlist.display()

dlist.remove_list()
dlist.display()
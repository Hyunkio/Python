class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    # 리스트의 앞에 노드를 추가하는 메서드
    def add_first(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # 리스트의 뒤에 노드를 추가하는 메서드
    def add_last(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    # 특정 인덱스에 노드를 삽입하는 메서드
    def insert_at(self, index, data):
        if index == 0:
            self.add_first(data)
            return

        new_node = Node(data)
        current = self.head
        for _ in range(index - 1):
            if current is None:
                raise IndexError("Index out of bounds")
            current = current.next

        new_node.next = current.next
        if current.next is not None:
            current.next.prev = new_node
        new_node.prev = current
        current.next = new_node

        if new_node.next is None:
            self.tail = new_node
            
    # 리스트의 첫 번째 노드를 삭제하는 메서드
    def remove_first(self):
        if self.head is None:
            raise IndexError("List is empty")
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    # 리스트의 마지막 노드를 삭제하는 메서드
    def remove_last(self):
        if self.tail is None:
            raise IndexError("List is empty")
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    # 특정 인덱스의 노드를 삭제하는 메서드
    def remove_at(self, index):
        if index == 0:
            self.remove_first()
            return

        current = self.head
        for _ in range(index):
            if current is None:
                raise IndexError("Index out of bounds")
            current = current.next

        if current == self.tail:
            self.remove_last()
        else:
            current.prev.next = current.next
            if current.next is not None:
                current.next.prev = current.prev
                
    # 리스트의 모든 노드를 순방향으로 출력하는 메서드
    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    # 리스트의 모든 노드를 역방향으로 출력하는 메서드
    def display_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")   
        
dlist = DoublyLinkedList()
dlist.add_last(10)
dlist.add_last(20)
dlist.add_last(30)
dlist.display_forward()  # 10 <-> 20 <-> 30 <-> None

dlist.add_first(5)
dlist.display_forward()  # 5 <-> 10 <-> 20 <-> 30 <-> None

dlist.remove_at(2)
dlist.display_forward()  # 5 <-> 10 <-> 30 <-> None

dlist.display_backward()  # 30 <-> 10 <-> 5 <-> None
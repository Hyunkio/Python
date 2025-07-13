class Node: #LinkedList 칸
  def __init__(self, data): 
      self.data = data 
      self.next = None 

class SinglyLinkedList: 
  def __init__(self):
      self.head = None 

  def append(self, data): #맨 뒤 데이터 추가
      new_node = Node(data) 
      
      if not self.head: 
          self.head = new_node
      else: 
        current = self.head
        while current.next: 
            current = current.next
        current.next = new_node 
        
  def insert_at(self, index, data):  #원하는 위치 데이터 삽입
      if index == 0: 
          new_node = Node(data)
          new_node.next = self.head 
          self.head = new_node
          return
      current = self.head
      for i in range(index - 1):
          if current is None:
              raise IndexError("Index out of bounds")
          current = current.next
      new_node = Node(data)
      new_node.next = current.next
      current.next = new_node
      
  def display(self):  #리스트 출력
      current = self.head
      while current: 
          print(current.data, end=" -> ") 
          current = current.next
      print("None") 
      
slist = SinglyLinkedList()
slist.append(10)
slist.append(20)
slist.append(30)
slist.display() #10 -> 20 -> 30 -> None

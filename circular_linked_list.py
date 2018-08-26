class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class CircularLinkedList:
    def __init__(self):
        #unlike LinkedList keep reference to tail as tail points to head
        self.tail = None 
        
    def display_list(self):
        current = self.tail.next   #pointer to first node
        while True:
            print(current.data)
            if current.next == self.tail.next: #means we reached last node
                break
            current = current.next
        print("***********")
        
    def insert_blanklist(self,item):
        node = Node(item)
        self.tail = node
        #tail should refer to itself as there is no other node
        self.tail.next = self.tail
        
    def insert_head(self,item):
        node = Node(item)
        node.next = self.tail.next #new node points to head node
        self.tail.next = node      #tail points to new head
        
    def insert_tail(self,item):
        node = Node(item)
        node.next = self.tail.next  #node points to head
        self.tail.next = node       #old tail points to node
        self.tail = node            #set tail pointer to node
        
    def insert_after_value(self,value,item):
        current = self.tail.next    #pointer to first node
        while True:
            if current.data == value:
                break
            current = current.next
            if current.next == self.tail.next:
                break
        node = Node(item)
        node.next = current.next
        current.next = node
        if current == self.tail:
            self.tail = node
            
    def delete_head(self):
        #delete first node of the list
        #increment pointer of self.last.next
        self.last.next = self.last.next.next
        
    def delete_tail(self):
        #find predecessor to last node
        current = self.last.next
        while True:
            current = current.next
            if current.next.next == self.tail.next:
                break
        #predecessor node now points to head
        current.next = self.tail.next
        #update tail node
        self.tail = current
        
    def delete_after_value(self,value):
        current = self.tail.next
        #find the node with the given value
        while current:
            if current.data == value:
                break
            if current.next == self.tail.next:
                break
            current = current.next
        current.next = current.next.next
        
    
        
        
            
        
        
            
    
        

#client code
#create a circular LL
node0 = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node0.next = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node0

cl = CircularLinkedList()
cl.tail = node4
cl.display_list()
cl.insert_head(10)
cl.display_list()
cl.insert_tail(20)
cl.display_list()
cl.insert_after_value(20,9)
cl.display_list()
cl.delete_after_value(3)
cl.display_list()

    



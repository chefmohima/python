class Node:
    #this represents node for a doubly linked-list
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def insert_in_emptylist(self,item):
        node = Node(item)
        self.head = node
        
    def insert_head(self,item):
        node = Node(item)
        node.next = self.head
        self.head.prev = node
        self.head = node
        
    def insert_tail(self,item):
        node = Node(item)
        #find last node
        current = self.head
        while current.next != None:
            current = current.next
        current.next = node
        node.prev = current
        
    def insert_after_value(self,value,item):
        node = Node(item)
        #get the node with data==value
        current = self.head
        while current:
            if current.data == value:
                break
            current = current.next
        node.prev = current
        node.next = current.next
        current.next.prev = node
        current.next = node
        
    def insert_before_value(self,value,item):
        node = Node(item)
        current = self.head
        while current:
            if current.data == value:
                break
            current = current.next
        node.prev = current.prev
        node.next = current
        current.prev.next = node
        current.prev = node
        
    def delete_head(self):
        #delete first node
        if self.head == None:
            #empty list
            return
        if self.head.next == None:
            #single node list
            self.head == None
            return
        self.head = self.head.next
        self.head.prev = None
        
    def delete_tail(self):
        #delete last node
        if self.head == None:
            #empty list
            return
        if self.head.next == None:
            #single node list
            self.head == None
            return
        #get last node
        current = self.head
        while current.next != None:
            current = current.next
        #set pointers
        current.prev.next = None
        
    def delete_node(self,value):
        pass
        
        
    def reverse_list(self):
        temp = None
        current = self.head
        while current:
            temp = current.prev
            current.prev = current.next #change the next and prev pointers
            current.next = temp
            current = current.prev
        self.head = temp.prev
        
        
        
    
    def display_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
        print("************")
        
node0 = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node0.next = node1
node1.prev = node0
node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2

#client code
dl = DoublyLinkedList()
dl.head = node0
#dl.display_list()
#dl.insert_head(10)
#dl.insert_tail(10)
#dl.display_list()
#dl.insert_after_value(0,10)
#dl.display_list()
#dl.insert_before_value(2,20)
dl.display_list()
dl.reverse_list()
dl.display_list()
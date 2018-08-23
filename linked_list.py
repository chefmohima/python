class Node:
    #this represents a single node in a linked list.
    #each node has data and pointer to the next node
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    #linkedlist class, has pointer to the first node in the linkedlist 
    def __init__(self):
        self.head = None
        
    def display_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
        
    def count_nodes(self):
        node_count = 0
        current = self.head
        while current:
            node_count += 1
            current = current.next
        return node_count
    
    def search(self,item):
        #return True if item is in the list
        current = self.head
        found = False
        while current and not found:
            if current.data == item:
                found = True
            current = current.next
        return found
        
    def insert_head(self,item):
        node = Node(item)
        if not self.head:
            self.head = node
        temp = self.head
        node.next = temp
        self.head = node
        
        
    
    def insert_tail(self,item):
        pass
    
    def insert_at_pos(self,pos,item):
        pass
    
    def insert_before_pos(self,pos,item):
        pass
    
    def insert_after_pos(self,pos,item):
        pass
        
    

#Client code to test the LinkedList class
node0 = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node0.next = node1
node1.next = node2
node2.next = node3
node3.next = node4

ll = LinkedList()
ll.head = node0

ll.display_list()
count = ll.count_nodes()
print("No. of nodes = ", count)
print (ll.search(4))
ll.insert_head(5)
ll.display_list()

        
    
    

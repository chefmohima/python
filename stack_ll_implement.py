##Linked list implementation of a stack
#Push and pop from same end of linked list
#top points to head of the list where elements are pushed/popped

class EmptyStackError(Exception):
    pass

class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
        
class Stack:
    
    def __init__(self):
        self.top = None
        
    def isEmpty(self):
        return self.top == None
        
    def size(self):
        if self.isEmpty():
            return 0
        n = 0
        while self.top is not None:
            n = n+1
            self.top = self.top.next
            
        return n
    
    def push(self,data):
        node = Node(data)
        node.next = self.top
        self.top = node
        
    def pop(self):
        if self.isEmpty():
            raise EmptyStackError("Stack is empty!")
        popped = self.top
        self.top = self.top.next
        return popped.data
        
    def peek(self):
        if self.isEmpty():
            raise EmptyStackError("Stack is empty!")
        return self.top.data
        
    def display(self):
        
        if self.isEmpty():
            raise EmptyStackError("Stack is empty!")
        
        t = self.top
        while t:
            print(t.data)
            t = t.next
        print("**********")
            

s = Stack()
s.push(10)
s.push(9)
s.push(8)
s.push(7)
s.push(6)
s.push(5)

s.display()

s.pop()
s.pop()

s.display()
            

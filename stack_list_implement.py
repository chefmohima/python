class Stack: 
    #list-based stack implementation
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def push(self,item):
        self.items.append(item)
        
    
    def pop(self):
        if self.items == []:
            raise EmptyStackError("Stack is empty!")
        else:
            item = self.items.pop()
            return item
    
    def display(self):
        print(self.items)
        print("********************")
        
    
    def peek(self):
        if self.items == []:
            raise EmptyStackError("Stack is empty!")
        else:
            print(self.items[-1])
            
#Client code to test stack operations
s = Stack()
s.push(10)
s.push(9)
s.push(8)
s.push(7)
s.display()
s.pop()
s.pop()
s.peek()
s.display()
        
    
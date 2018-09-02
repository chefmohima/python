#List implementation of a queue
#Add elements at rear end and remove elements from front

class EmptyQueueError(Exception):
    pass

class Queue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
        
    def size(self):
        return len(self.items)
        
    def enqueue(self,data):
        self.items.append(data)
        
    def dequeue(self):
        if self.isEmpty():
            raise EmptyQueueError
        e = self.items.pop(0)
        return e
    
    def display(self):
        if self.items == []:
            print ("Queue is empty")
        else:
            print(self.items)
            print("***********")
            
q = Queue()
q.enqueue(10)
q.enqueue(9)
q.enqueue(8)
q.enqueue(7)
q.display()
#should print 10,9,8,7
q.dequeue()
q.dequeue()
q.display()   
#should print 8.7
    

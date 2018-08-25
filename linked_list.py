class Node:
    # this represents a single node in a linked list.
    # each node has data and pointer to the next node
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    # linkedlist class, has pointer to the first node in the linkedlist
    def __init__(self):
        self.head = None

    def display_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
        print("********************")

    def count_nodes(self):
        node_count = 0
        current = self.head
        while current:
            node_count += 1
            current = current.next
        return node_count

    def search(self, item):
        # return True if item is in the list
        current = self.head
        found = False
        while current and not found:
            if current.data == item:
                found = True
            current = current.next
        return found

    def insert_head(self, item):
        node = Node(item)
        # if list is empty self.head = node
        if not self.head:
            self.head = node
        # temp = self.head
        node.next = self.head
        self.head = node

    def insert_tail(self, item):
        node = Node(item)
        # find the last node
        current = self.head
        while current.next:
            # prev = current
            current = current.next
        last = current
        # set next pointer of last node
        last.next = node

    def insert_before_value(self, value, item):
        # insert a new node with data = item before the node that has data=value
        node = Node(item)

        # find the predecessor to node with data=item
        current = self.head
        while current:
            if current.next.data == value:
                break
            current = current.next

        node.next = current.next
        current.next = node

    def insert_after_value(self, value, item):
        # insert a new node with data = item before the node that has data=value
        node = Node(item)

        # find node with data=value
        current = self.head
        while current:
            if current.data == value:
                break
            current = current.next
        node.next = current.next
        current.next = node

    def insert_at_index(self, index, item):
        node = Node(item)

        if index == 0:
            # insert at head of the list
            node.next = self.head
            self.head = node

        i = 1
        current = self.head
        # get the node at index-1
        while current:
            if i == index - 1:
                break
            i = i + 1
            current = current.next
        node.next = current.next
        current.next = node

    def delete_first_node(self):
        self.head = self.head.next

    def delete_last_node(self):
        # find the predecessor to last node
        current = self.head
        while current:
            if current.next.next == None:
                break
            current = current.next

        # set the next node of the predecessor node to null
        current.next = None

    def delete_node(self, value):
        # if it is the first node
        current = self.head
        if current.data == value:
            self.head = self.head.next
            return

        # find the predecessor to the node with data == value
        while current:
            if current.next.data == value:
                break
            current = current.next
        # set next node of predecessor node
        current.next = current.next.next

    def reverse_list(self):
        current = self.head
        prev = None
        while current:
            temp = current.next
            current.next = prev #reverse link direction
            prev = current      #move forward prev and current pointers
            current = temp
        self.head = prev        #assign new head of list

    def detect_cycle(self):
        s = set()
        current = self.head
        while current:
            if current in s:
                return True
            s.add(current)
            current = current.next
        return False


# Client code to test the LinkedList class
# build linkedlist
node0 = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node0.next = node1
node1.next = node2
node2.next = node3
node3.next = node4
#create cycle
#node4.next = node1

ll = LinkedList()
ll.head = node0
############################
#ll.display_list()
# ll.insert_tail(10)

# ll.display_list()
# count = ll.count_nodes()
# print("No. of nodes = ", count)
# print (ll.search(4))
# ll.insert_head(5)
# ll.display_list()
# ll.insert_tail(10)

# ll.display_list()
# print("******")
# ll.insert_at_pos(0,100)
# ll.display_list()
# ll.insert_before_value(1,10)
# print("******")
# ll.display_list()
# ll.insert_after_value(0,0)
# ll.display_list()
# ll.insert_at_index(2,10)
# ll.delete_first_node()
# ll.delete_last_node()
# ll.display_list()
#ll.delete_node(0)
#ll.reverse_list()


#ll.display_list()
print(ll.detect_cycle())
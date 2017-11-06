class Node(object):

    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList(object):
    
    head = None
    tail = None

    def append(self, data):
        new_node = Node(data,prev=self.tail)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if self.head is None:
            self.head = self.tail

    def remove(self):
        if self.tail is None:
            return None
        data = self.tail.data
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        if self.head == self.tail:
            self.head = None

    def show(self):
        x = self.head
        print("None <-> ", end="")
        while x:
            print(x.data, "<-> ", end="")
            x = x.next
print(None)

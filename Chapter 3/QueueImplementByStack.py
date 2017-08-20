

class Node(object):
    def __init__(self,data,Next=None):
        self.data=data
        self.next=Next


class Stack(object):
    def __init__(self,head=None):
        self.head=head

    def push(self,data):
        self.head=Node(data,self.head)

    def pop(self):
        if self.head is None:
            raise Exception("Stack is empty")
        else:
            data=self.head.data
            self.head=self.head.next
            return data

    def peek(self):
        if self.head is None:
            raise Exception("stack is empty")
        else:
            return self.head.data

    def is_empty(self):
        return self.head is None

class Myqueue(object):
    def __init__(self):
        self.enqueue=Stack()
        self.dequeue=Stack()
        self.order_enqueue=True

    def enfiler(self,data):
        if not self.order_enqueue:
            while not self.dequeue.is_empty():
                self.enqueue.push(self.dequeue.pop)
        self.order_enqueue=True
        self.enqueue.push(data)

    def defiler(self):
        if self.order_enqueue:
            while not self.enqueue.is_empty():
                self.dequeue.push(self.enqueue.pop())
        self.order_enqueue=False
        if self.dequeue.is_empty():
            raise Exception("stack is empty")
        return self.dequeue.pop()


    def show(self):
        if self.order_enqueue:
            while not self.enqueue.is_empty():
                self.dequeue.push(self.enqueue.pop())
        self.order_enqueue=False
        if self.dequeue.is_empty():
            raise Exception("stack is empty")
        return self.dequeue.peek()




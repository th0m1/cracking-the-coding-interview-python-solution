class Node(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack(object):

    def __init__(self, head=None):
        self.head = head

    def push(self,data):
        self.head=Node(data,self.head)

    def pop(self):
        if self.head is None:
            raise Exception("stack is empty")
        else:
            data=self.head.data
            self.head=self.head.next
            return data
    def peek(self):
        if self.head is None:
            raise Exception("stack is empty")
        else:
            data=self.head.data
            return data

    def is_empty(self):
        return self.head is None

    def printStack(self):
        x=self.head
        while x:
            print(x.data)
            x=x.next

    def copy(self):
        cp=Stack()
        x=self.head
        while x:
            cp.push(x.data)
            x=x.next
        return cp



def sort(stack):
    s=stack.copy()
    res=Stack()
    while not s.is_empty:
        tmp=s.pop()
        while not res.is_empty and tmp>res.peek():
            s.push(r.pop())
        res.push(tmp)
    while not res.is_empty():
        s.push(res.pop())
    return s



            

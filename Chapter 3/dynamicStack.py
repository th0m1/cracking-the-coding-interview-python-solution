
class Node(object):
    def __init__(self,data,Next=None):
        self.data=data
        self.next=Next


class Stack(object):

    def __init__(self,head=None):
        self.head=None
        self.size=0

    def push(self,data):
        if self.head is None:
            self.head=Node(data)
            self.size+=1
        else:
            self.head=Node(data,self.head)
            self.size+=1

    def is_empty(self):
        if self.head is None or self.size==0:
            raise Exception("stack is empty")
        return False

    def pop(self):
        if self.is_empty() == False:
            data=self.head.data
            self.head=self.head.next
            self.size-=1
        else:
            raise Exception("stack is empty")
    def get_size(self):
        count=0
        x=self.head
        while x:
            x=x.next
            count+=1
        return count

    def show(self):
        x=self.head
        while x:
            print(x.data)
            x=x.next




class StackOfPlates(object):

    def __init__(self,Stacksize):
        self.stacksize=Stacksize
        self.arrayofstack=[]

    def push(self,data):
        if len(self.arrayofstack)==0 or self.arrayofstack[-1].get_size()==self.stacksize:
            self.arrayofstack.append(Stack())
        self.arrayofstack[-1].push(data)

    def pop(self):
        if len(self.arrayofstack)==0:
            return None
        data=self.arrayofstack[-1].pop()
        if self.arrayofstack[-1].get_size()==0:
            self.arrayofstack[:-1]
        return self.arrayofstack[-1].pop()


    def popAt(self,index):
        if len(self.arrayofstack)==0:
            raise Exception("stack is empty")
        if index>len(self.arrayofstack)-1:
            raise IndexError("index out of range")
        else:
            data=self.arrayofstack[index].pop()
            if self.arrayofstack[index].get_size()==0:
                del self.arrayofstack[index]
            else:
                self.remplir_stack(index)
            return data

    def remplir_stack(self,index):
        while index<len(self.arrayofstack)-1:
            x=arrayofstack[-1].head
            prev=None
            if x.next:
                while x.next:
                    prev=x
                    x=x.next
                prev.next=x.next
            else:
                del self.arrayofstack[index+1]
            self.arrayofstack[index].push(x,data)
            index+=1
            





        
            
        
        
        
        
            
            
    

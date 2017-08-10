
class node:
    def __init__(self,data,track_min,nexte=None):
        self.data=data
        self.track_min=track_min
        self.next=nexte

class stack_with_min:
    def __init__(self,head=None):
        self.head=head
        self.currentMin=None

    def push(self,data):
        if self.head is None:
            self.head=node(data,data)
            self.currentMin=data
        elif data<self.head.track_min:
            self.head=node(data,data,self.head)
        else:
            self.head=node(data,self.head.track_min,self.head)
                

    def pop(self):
        if self.head is None:
            raise Exception("stack is empty")
        dataa=self.head.data
        self.head=self.head.next
        return dataa

    def minn(self):
        if head is None:
            raise Exception("stack is empty")
        return head.track_min




    
                
        
    

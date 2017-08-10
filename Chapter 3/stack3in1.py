class TreeInOne:

    def __init__(self,stacksize,stacknumber):
        self.stacksize=stacksize
        self.stacknumber=stacknumber
        self.array=[None for _ in range(self.stacksize*self.stacknumber)]
        self.indexofstack=[i*(self.stacksize) for i in range(self.stacknumber)]

    def full(self,stacknb):
        if self.indexofstack[stacknb-1]==(stacknb*self.stacksize):
            raise Exception("stack is full")
        else:
            return True
    def push(self,data,stacknb):
        if self.full(stacknb):
            self.array[self.indexofstack[stacknb-1]]=data
            self.indexofstack[stacknb-1]+=1
        else:
            raise Exception("stack is full")

    def empty(self,stacknb):
        if self.indexofstack[stacknb-1]==((stacknb-1)*self.stacksize):
            raise Exception("stack is empty")
        else:
            return True

    def pope(self,stacknb):
        if self.empty(stacknb):
            data=self.array[self.indexofstack[stacknb-1]]
            self.array[self.indexofstack[stacknb-1]]=None
            self.indexofstack[stacknb-1]-=1
        else:
            raise Exception("stack is empty")
    def showstack(self,stacknb1):
        if self.empty(stacknb1):
            data=self.array[self.indexofstack[stacknb1-1]-1]
            return data
        else:
            raise Exception("stack is empty")
        

teststack=TreeInOne(100,3)
teststack.full(1)
teststack.push(10,1)
teststack.push(10,1)
teststack.push(10,1)
teststack.push(10,2)
teststack.push(10,2)
teststack.push(10,2)
teststack.showstack(1)
#teststack.showstack(3)



            
        

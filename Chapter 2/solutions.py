
class Node(object):
      def __init__(self,data,Next=None):
            self.data=data
            self.next=Next

class LinkedList(object):
      def __init__(self,head):
            self.head

      def push(self,data):
            self.head=Node(data,self.head)

      def pop(self):
            if self.head is None:
                  raise Exception("stack is full")
            data=self.head.data
            self.head=self.head.next
            return data
      def full(self):
            if self.head is None:
                  raise Exception("list full")
            return False

      def removeDups(self):
            x=self.head
            runner=x
            while x:
                  while runner.next:
                        if x.data==runner.next.data:
                              runner.next=runner.next.next
                        else:
                              runner=runner.next
                  x=x.next
                  runner=x

      def removeDupsBuffer(self):
            x=self.head
            seen=set(x.data)
            while x.next:
                  if x.next.data not in seen:
                        seen.add(x.next.data)
                        x=x.next
                  else:
                        x.next=x.next.next
            return self

      def kthToLast(self,k):
            current=self.head
            runner=self.head
            for i in range(k):
                  runner=runner.next
            while runner:
                  runner=runner.next
                  current=current.next
            return current

      def deleteMidNode(self,node):
            if node is None or node.next is None:
                  return False
            node.data=node.next.data
            node.next=node.next.next


      def Partition(self,pivot):
            x=self.head
            prev=None
            while x:
                  if prev and x.data<pivot:
                        prev.next=x.next
                        self.head=x
                        x=prev.next
                  else:
                        prev=x
                        x=x.next
            return head
                        
                        
                        
            
            
            
            
            
                        
                  
                        
                          
                        
            
                  
                  
            
            

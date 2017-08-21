

class NodeBST(object):

      def __init__(self,key,val):
            self.key=key
            self.val=val
            self.left=None
            self.right=None

class BST(object):

      def __init__(self,root=None):
            self.root=root
            self.size=0

      def ajout(self,key,val):
            self.root=self._ajout(self.root,key,val)
            self.size+=1
            return self.root

      def _ajout(self,x,key,val):
            if x is None:
                  return NodeBST(key,val)
            if key<x.key:
                  x.left=self._ajout(x.left,key,val)
            elif key>x.key:
                  x.right=self._ajout(x.right,key,val)
            else:
                  x.val=val
            return x

      def get(self,key):
            x=self._get(self.root,key)
            if x is None:
                  return None
            else:
                  return x.val

      def _get(self,x,key):
            if x is None :
                  return None
            if key<x.key:
                  return self._get(x.left,key)
            elif key>x.right:
                  return self._get(x.right,key)
            else:
                  return val

      def printBFS(self):
            queue =[self.root]
            while len(queue) !=0:
                  x=queue.pop()
                  if x:
                        print(x.key)
                        queue.insert(0,x.left)
                        queue.insert(0,x.right)
                  elif len(queue) != 0:
                        print(x)
            print(None)

class BST2(BST):

      def put_ary(self,ary):
            if ary is not None:
                  self.root=self._put_ary(ary,0,len(ary)-1)
                  return self.root
      def _put_ary(self,ary,start,end):
            if end<start:
                  return None
            mid=(start+end)//2
            x=NodeBST(ary[mid],None)
            x.left=self._put_ary(ary,start,mid-1)
            x.right=self._put_ary(ary,mid+1,end)
            return x

if __name__ == "__main__":
      t=BST2()
      ary = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
      t.put_ary(ary)
      t.printBFS()


def createBST(tree,array):
    _createBST(tree,array,0,len(array)-1)

def _createBST(tree,array,start,end):
     if start<=end:
           mid=(start+end)//2
           tree.ajout(array[mid],0)
           _createBST(tree,array,start,mid-1)
           _createBST(tree,array,mid+1,end)

if __name__ == "__main__":
    t = BST()
    ary = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    createBST(t, ary)
    t.printBFSs()

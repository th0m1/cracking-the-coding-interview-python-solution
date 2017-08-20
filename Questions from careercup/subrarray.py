#Given an array of 'array ranges', return an optimized array by
#   deleting subarrays.
#INPUT: [(2,6),(3,5),(7,21),(20,21)]
#  OUTPUT: [(2,6),(7,21)]

#OUTPUT: [(2,6),(7,21)]




def subrange1(array):
      if array is None or len(array)==1:
            return array
      res=[]
      array.sort(key=lambda x: x[0])
      i=0
      while i < len(array)-1:
            res.append(array[i])
            if array[i+1][1]<=array[i][1]:
                  i+=2
            else:
                  i=i+1
      return res

subrange1( [(2,6),(3,5),(7,21),(20,21)])
                        

    

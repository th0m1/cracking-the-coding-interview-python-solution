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
      for i in range(len(array)-1):
            if array[i]:
                  res.append(array[i])
                  if array[i+1][1]<=array[i][1]:
                        array[i+1]=None
      return res

subrange1( [(2,6),(3,5),(7,21),(20,21)])
                        

    

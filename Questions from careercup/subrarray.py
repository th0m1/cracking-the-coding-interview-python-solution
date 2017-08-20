#Given an array of 'array ranges' (rs), return an optimized array by
#   deleting subarrays. Time complexity O(n*log(n)).
#>>> subrange([(2, 6), (3, 5), (20, 21), (7, 21)])
#    [(2, 6), (7, 21)]
#    >>> subrange([(10, 13), (1, 8), (2, 6), (15, 18), (12, 18)])
#    [(1, 8), (10, 13), (12, 18)]



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

subrange1([(10, 13), (1, 8), (2, 6), (15, 18), (12, 18)])
                        

    

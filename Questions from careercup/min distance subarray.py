#given a long string "s" and short strings t1,t2,t3
#find the shotest string of s that contains t1,t2 and t3

def minsubstr(s,t1,t2,t3):
      index_t1=s.index(t1)
      index_t2=s.index(t2)
      index_t3=s.index(t3)
      start=min(index_t1,index_t2,index_t3)
      end =max(index_t1,index_t2,index_t3)
      last_len=max(len(t1),len(t2),len(t3))-1
      return [start,end+last_len-1]



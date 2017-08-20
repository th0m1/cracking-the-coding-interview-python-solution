
def uniquechar(s):
    long=len(s)
    count=dict()
    for i in range(long):
        count[s[i]]+=1
        if count[s[i]]>1:
            return False


def uniquechar_without(s):
    long=ord(z)-ord(a)+1
    array=[i for i in range(long)]
    for i in range(len(s)):
        array[ord(s[i])-ord("z")+26]=True
        if array[ord(s[i])-ord("z")+25]:
            return False
    return True



#check permutation given 2 strings write method to decide if one is permutation of the other


def checkpermutation(s1,s2):
    if len(s1) != len(s2):
        return False
    ss1=sorted(s1)
    ss2=sorted(s2)
    return ss1==ss2

def checkpermutation2(s1,s2):
      if len(s1) != len(s2):
          return False
      count=dict()
      for i in range(len(s1)):
            count[s1[i]]+=1
      for i in range(len(s2)):
            count[s2[i]]-=1
            if count[s2[i]]<0:
                  return False
      return True


#Urlify write method to replace space with %20

def urlify(s,length):
      length_s=len(s)
      for i in range(reversed(length)):
            if s[i]==" ":
                  s[length_s-3:length_s]="%20"
            else:
                  s[length_s-1:length_s]=s[i]
      return s

#palindrome permutation check if palindrome

def checkpalindromeperm(s):
      chars=dict()
      oddcount=0
      for i in s:
            if not i.isalnum():
                  continue
            try:
                  chars[i]+=1
            except KeyError:
                  chars[i]=1
            if chars[i]%2==1:
                  oddcount+=1
            else:
                  oddcount-=1
      return oddcount<2
                  
      
#one way

def oneway(s1,s2):
      if len(s1)==len(s2):
            return replace(s1,s2)
      if len(s1)+1==len(s2):
            return edit(s1,s2)
      if len(s2)+1==len(s1):
            return edit(s2,s1)
      return False

def replace(s1,s2):
      edited=False
      for i1 ,i2 in zip(s1,s2):
            if i1 != i2:
                  if edited:
                        return False
                  edited=True
      return True

def edit(s1,s2):
      edited=False
      i,j=0,0
      while i<len(s1) and j<len(s2):
            if s1[i] != s2[j]:
                  if edited:
                        return False
                  edited=True
                  j=j+1
            else:
                  i+=1
                  j+=1
      return True

# string compression

def strcompress(s):
      res=""
      count=0
      for i in range(1,len(s)):
            count+=1
            if s[i-1] != s[i]:
                  res=res+s[i-1]+str(count)
                  count=0
      res=res+s[-1]+str(count+1)
      return res if len(res)<len(s) else s


# rotate matrice 90 degres


def rotate90matrice(M):
      I=len(M)
      J=len(M[0])
      for layer in range(I//2):
            first,last=layer,I-1-layer
            for j in range(first,last):
                  top=M[layer][j]
                  M[layer][j]=M[-i-1][layer]
                  M[-i-1][layer]=M[layer-1][-i-1]
                  M[layer-1][-i-1]=M[j][-layer-1]
                  M[j][-layer-1]=top
      return M


#zero matrice


def zeromatrice(M):
      cols=[]
      rows=[]
      for i in range(len(M)):
            for j in range(len(M[0])):
                  if M[i][j]==0:
                        cols.append(j)
                        rows.append(i)
      for row in rows:
            for j in range(len(M[0])):
                  M[row][j]=0
      for col in cols:
            for i in range(len(M)):
                  M[i][col]=0

      return M
#string rotation

def stringrotation(s,sub):
      s=s+s
      return sub in s


            
                        
                        
      



                  
                  
            
            
      
      
                  

            
            
            
            
            
                              
                        
                        
            
            
            
      
            
      
      
      
    

def array_left_rotation(a, n, k):
    if k >= n:
        return a
    res=[]
    res=a[k:]+a[:k]
    return res


array_left_rotation(list(range(10)),11,5)



            


if __name__=='__main__':
    n= int(input())
    k= int(input())
    list1=[]
    for i in range(n):
        list1.append(int(input()))
    list1.sort()
    
    minval=max(list1)
    for i in range(n-k):
        #print(i,i+k,max(list1[i:i+k]),min(list1[i:i+k]))
        newval=list1[i+k-1]-list1[i]
        if(newval<minval):
            minval=newval
            
    print(minval)
        
    
        
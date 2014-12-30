
if __name__=='__main__':
    string= input()
    myset= set(string)
    count=[]
    oddcount=0
   
    for i in myset:
        if string.count(i)%2==1:
            oddcount+=1
 
    if oddcount>1:
        print('NO')
    else:
        print('YES')
    
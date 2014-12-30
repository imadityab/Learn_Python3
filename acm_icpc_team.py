def gettcount(str1,str2):
    num1=int(str1,2)
    num2=int(str2,2)
    num3= num1 | num2
    
    tc=str(bin(num3)[2:])
    return tc.count('1')


if __name__=='__main__':
    args=input().split(' ')
    pcount=int(args[0])
    tcount=int(args[1])
    tkarray=[]
    maxtcount=[]
    
    for i in range(pcount):
        tkarray.append(input())
    for i in range(pcount):
        maxtcount.append(0)
        for j in range(i+1,pcount):
            res=gettcount(tkarray[i],tkarray[j])
            if(res>maxtcount[i]):
                maxtcount[i]=res
    print(max(maxtcount))
    print(maxtcount.count(max(maxtcount)))
            
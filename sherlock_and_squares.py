import math

if __name__=='__main__':
    test_count= int(input())
    for i in range(test_count):
        L,M = str(input()).split(' ')
        ans= math.floor(math.sqrt(int(M))) - math.floor(math.sqrt(int(L)))
        if(math.sqrt(int(L))%1==0):
            ans+=1
        print(ans)  
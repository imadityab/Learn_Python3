import math

T = int(input())

for i in range(T):

    N,C,M = str(input()).split()
    chocnum= math.floor(int(N)/int(C))
    total = chocnum
    rem = 0;
   
    while(chocnum>= int(M)):
        morenum=math.floor(chocnum/int(M))
        rem= chocnum%int(M)
        total+=morenum
        chocnum = morenum + rem
        
    # Compute Answer
    print(total)

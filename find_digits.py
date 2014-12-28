import math

count = int(input())

for i in range(count):
    num= int(input())
    cnt=0
    nump= num
    while(nump>=1):
        digit=nump%10
        if(digit!=0 and num%digit==0):
            cnt+=1
        nump=math.floor(nump/10)
    print(cnt)
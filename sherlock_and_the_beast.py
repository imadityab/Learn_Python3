
def getnumber(leng):
    num5 = -1
    for i in range(leng+1):
        if(i % 3 == 0 and (leng - i) % 5 == 0):
            num5 = i
    return num5

if __name__=='__main__':
    testnum = int(input())
    for i in range(testnum):
        num_len = int(input())
        if(num_len<3):
            print('-1')
        else:
            a = getnumber(num_len)
            if(a == -1):
                print('-1')
            else:
                print('5'*a + '3'*(num_len-a))
                
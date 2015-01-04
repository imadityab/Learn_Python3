from fractions import gcd
from functools import reduce

def gcd1(L):
    return reduce(gcd, L)

if __name__=='__main__':
    num_test= int(input())
    for i in range(num_test):
        num= input()
        list= [int(x) for x in input().split()]
        if gcd1(list)==1:
            print('YES')
        else:
            print('NO')
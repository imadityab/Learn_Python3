import math

def getdiff(char1,char2):
    #print(char1,char2)
    return abs(ord(char1)-ord(char2))
    
def num_reductions(test):
    red=0
    for j in range(0,math.ceil(len(test)/2)):
        red+=getdiff(test[j],test[-j-1])
    return red    

if __name__=='__main__':
    for i in range(int(input())):
        print(num_reductions(input()))
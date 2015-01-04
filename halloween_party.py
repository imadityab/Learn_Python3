if __name__=='__main__':
    test_num = int(input())
    for i in range(test_num):
        num_cuts= int(input())
        chocs=0
        if(num_cuts%2==0):
            chocs= (num_cuts/2)*(num_cuts/2)
        else:  
            chocs= ((num_cuts-1)/2)*((num_cuts+1)/2)
        if(num_cuts<2):
            print("0")
        else:
            print(int(chocs))
            
if __name__=='__main__':
    test_num= int(input())
    for i in range(test_num):
        num_stone= int(input())
        num_a= int(input())
        num_b= int(input())
        listo=[]
        for j in range(num_stone):
            num=j*num_a+(num_stone-j-1)*num_b
            listo.append(num)
        listo.sort()
        set_result = set(listo)
       
        for item in sorted(set_result):
            print(item, '', end='')
        print()
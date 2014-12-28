def isFibo(num):
    num1=0
    num2=1
    add= 1
    while(add<num):
        num1=num2
        num2=add
        add= num1 + num2
    if(add==num):
        return True
    else:
        return False

testCount = int(input())

for i in range(testCount):
    num = int(input())
    
    if isFibo(num):
        print('IsFibo')
    else:
        print('IsNotFibo')
        

        
    
    
       
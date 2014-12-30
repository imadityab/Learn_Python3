import math

if __name__=='__main__':
    numbers = input().split(' ')
    jar_count=int(numbers[0])
    trans_count=int(numbers[1])
    total = 0
    for i in range(trans_count):
        element= input().split(' ')
        total+=(int(element[1])+1-int(element[0]))*int(element[2])
    print(math.floor(total/jar_count))
	
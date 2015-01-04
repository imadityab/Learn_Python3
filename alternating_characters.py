def num_del(string):
    count = 0
    mylist = list(string)
    for j in range(len(string) - 1):
        if(mylist[j] == mylist[j + 1]):
            count += 1
    return count

if __name__== '__main__':

    for i in range(int(input())):
        test = input()
        print(num_del(test))

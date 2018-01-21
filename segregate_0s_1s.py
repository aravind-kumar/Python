def sort0s1s(input):
    i=0
    j=len(input)-1
    while(i<j):
        while(input[i]==0):
            i=i+1
        while(input[j]==1):
            j=j-1
        if(i<j):
            input[i],input[j] = input[j],input[i]

if __name__ == '__main__' :
    arr = [int(x) for x in input().split()]
    sort0s1s(arr)
    print(arr)

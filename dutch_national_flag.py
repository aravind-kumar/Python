def dutchNational(input):
    wall1=0
    wall2=0
    wall3=len(input)-1
    while(wall2<=wall3):
        if(input[wall2] == 0):
            input[wall2],input[wall1] = input[wall1],input[wall2]
            wall2+=1 
            wall1+=1 
        elif(input[wall2] == 1):
            wall2+=1
        elif(input[wall2] == 2):
            input[wall2],input[wall3] = input[wall3],input[wall2]
            wall3-=1

    print(arr)

if __name__ == '__main__':
    arr = [int(x) for x in input("Enter the input").split()]
    dutchNational(arr)
    print(arr)

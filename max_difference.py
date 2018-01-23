def maxDifference(arr):
    maxDif = arr[0]
    presentMin = arr[1]-arr[0]
    for x in arr[1:]: 
        maxDif=max(maxDif,x-presentMin)
        presentMin=min(presentMin,x)
    return maxDif

if __name__ == '__main__':
#    arr=[int(x) for x in input("Enter the input").split()]
    arr=[2, 3, 10, 6, 4, 8, 1]
    print(maxDifference(arr))

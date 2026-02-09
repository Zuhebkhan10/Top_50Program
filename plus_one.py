# Add one to number array

def plus_one(arr):
    n=len(arr)

    for i in range(n-1,-1,-1):
        if arr[i]<9:
            arr[i]+=1
            return arr
        arr[1]=0

    return [1]+arr
arr=[1,2,6]

print(plus_one(arr))

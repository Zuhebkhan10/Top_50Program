# Largest sum contiguous subarray

def maximum_subarray(arr):
    mx=arr[0]
    current=arr[0]

    for i in range(1,len(arr)):
        current=max(arr[i],current+arr[i])
        mx=max(mx,current)
    return mx

# arr=[10,11,2] output is the 23
arr=[10-5,2,10] #output is the 5+2+10=17

print("Largest sum contiguous subarray",maximum_subarray(arr))

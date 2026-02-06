# In place remove duplicates
arr = list(map(int, input("Enter elements: ").split()))
n = len(arr)

if n == 0:
    print("Empty list")
else:
    index = 1
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            arr[index] = arr[i]
            index += 1

    print("Array after removing duplicates:",arr[:index])


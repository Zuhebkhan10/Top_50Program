nums=[1,2,4,5,6,8]
target=6

def search_position(nums,target):
    for i in range(len(nums)):
        if nums[i]>=target:
            return i
    return len(nums)

print(search_position(nums,target))
# find two indices whose values sum to target.

def two_sum(nums, target):
    seen = {}  # value -> index
    for i, num in enumerate(nums):
       needed = target - num
       if needed in seen:
           return [seen[needed], i]
       seen[num] = i

nums = [2, 7, 11, 15,30]
target = 45

print(two_sum(nums, target))

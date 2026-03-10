# Write a Python program to find the number of distinct ways to reach the top of the staircase.

# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can climb either:
# 1 step, or
# 2 steps
# Return the number of distinct ways you can climb to the top.


def climb_stairs(n):
    if n<=2:
        return n

    f=1
    s=2

    for i in range(3,n+1):
        t=f+s
        f=s
        s=t

    return s

steps=int(input("Enter number of stairs "))
ways=climb_stairs(steps)

print("Number of ways to climb:",ways)




# Step 1 → 1 way
# Step 2 → 2 ways
# Step 3 → 1+2 = 3
# Step 4 → 2+3 = 5
# Step 5 → 3+5 = 8

# previous two stairs count the output
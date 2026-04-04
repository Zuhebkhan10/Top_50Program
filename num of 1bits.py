# count the number of set bits 1s in the binary representation of a number in python

num=15
count=0

while num>0:
    count+= num & 1
    num=num>>1

print(count
      )

# checks last bit using n & 1, then shifts right
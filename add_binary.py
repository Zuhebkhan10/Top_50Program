# Add two binary strings.

a="110"
b="101"

sum_bin=(bin(int(a,2)+int(b,2))[2:])
print(sum_bin)

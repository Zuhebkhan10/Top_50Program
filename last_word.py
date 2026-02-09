# Length of the last word in string.

s=input("Enter a String:")

words=s.strip().split()
print("Length of last word",len(words[-1]))

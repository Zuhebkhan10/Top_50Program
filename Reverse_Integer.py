# Reverse digits of an integer.
i=int(input("Enter a number"))
reverse=0

while i !=0:
    digit=i%10
    reverse=reverse*10+digit
    i=i//10
print("Reversed number is",reverse)
#Check if number reads same backward.
num=int(input("Enter the number"))

temp=num
res=0
while num>0:
    res=res*10+num%10
    num=num//10

if temp==res:
    print("Palindrome number")
else:
    print("Not a Palindrome number")


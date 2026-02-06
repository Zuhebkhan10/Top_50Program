# Check balanced brackets.
def is_balanced(s):
    stack=[]
    paris={')':'(','}':'{',']':'['}

    for i in s:
        if i in '({[':
            stack.append(i)
        elif i in ')}]':
            if not stack or stack.pop()!=paris[i]:
                return False

    return len(stack)==0

s=input("Enter brackets: ")

if is_balanced(s):
    print("Balanced")
else:
    print("Not Balanced")


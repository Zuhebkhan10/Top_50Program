# Longest common prefix:
import string

# Find common prefix among string

def prefix(strs):
    if not strs:
        return ""

    pre=strs[0]

    for i in strs[1:]:
        while not i.startswith(pre):
            pre=pre[:-1]
            if pre=="":
                return ""
    return pre
w=['flower','flow','flight']
m=['apple','april','appex']

print(prefix(w))
print(prefix(m))

 
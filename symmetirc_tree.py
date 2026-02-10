# Determine whether a binary tree is symmetric around its corner.
from operator import truediv


class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def isSymmetric(root):
    def mirror(a,b):
        if not a and not b:
            return True
        if not a or not b:
            return False
        return a.val==b.val and mirror(a.left,b.right) and mirror(a.right,b.left)
    return mirror(root.left,root.right)

root=Node(1)
root.left=Node(2)
root.right=Node(2)




print(isSymmetric(root))

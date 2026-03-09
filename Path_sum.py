# check if a root to leaf path exits such that the sum of node values equals a given target
class Node:
    def __init__(self,val):
        self.val= val
        self.left=None
        self.right=None

def pathSum(root,target):
    if root is None:
        return False

    if root.left is None and root.right is None:
        return target==root.val

    remaining=target-root.val
    return pathSum(root.left,remaining )or pathSum(root.right,remaining)

root=Node(5)
root.left=Node(4)
root.right=Node(8)
root.left.left=Node(11)
# root.left.left=Node(30)
root.right.left=Node(13)
root.right.right=Node(4)

target=20
if pathSum(root,target):
    print("Path Exists")
else:
    print("Path does not exists")

# Example Tree
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  / \
# 30  12


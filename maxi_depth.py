# Find the maximum depth or height of a binary tree.
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

    def depth(root):
        if root is None:
            return 0

        left_depth= Node.depth(root.left)
        right_depth= Node.depth(root.right)

        return 1+max(left_depth,right_depth)

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)

print(Node.depth(root))



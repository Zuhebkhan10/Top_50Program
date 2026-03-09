# check weather a binary tree i height-balanced meaning the height difference is not more than one.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

def isBalanced(root):
    if root is None:
        return True

    left_height = height(root.left)
    right_height = height(root.right)

    if abs(left_height - right_height) > 1:
        return False

    return isBalanced(root.left) and isBalanced(root.right)

# Balanced tree
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)

print("Balanced Tree:", isBalanced(root1))

# Unbalanced tree
root2 = Node(1)
root2.left = Node(2)
root2.left.left = Node(3)

print("Unbalanced Tree:", isBalanced(root2))

# Idea to Solve the Problem
# Find the height of left subtree
# Find the height of right subtree
# Check the difference
# Recursively check for left and right subtrees


# # convert a sorted array into a height-balanced binary search tree
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def BST_Sorted(arr):
    # Base case: if the array is empty, this branch is done
    if not arr:
        return None

    # Pick the middle element to ensure balance
    mid = len(arr) // 2
    root = Node(arr[mid])

    # Recursively build the subtrees
    root.left = BST_Sorted(arr[:mid])
    root.right = BST_Sorted(arr[mid+1:])
    return root

# Test data

arr = [-10, -3, 12, 5, 9]
root = BST_Sorted(arr)

# Verification: Printing the root value
print(f"Root of the BST: {root.val}")


# A height-balanced BST can be created from a sorted array by repeatedly choosing the middle element as the root.
# Time: O(n)
# Space: O(log n) (recursion stack for balanced tree)
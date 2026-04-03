# Remove duplicates from linked list
from pydantic_core.core_schema import none_schema


# Easy case because duplicates are next to each other.
# Traverse the list
# If current value == next value → skip the next node

class Node:
    def __init__(self):
        self.data=data
        self.next=
# Remove duplicates from linked list
from pydantic_core.core_schema import none_schema


# Easy case because duplicates are next to each other.
# Traverse the list
# If current value == next value → skip the next node

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def remove_dup(head):
    cur=head

    while cur and cur.next:
        if cur.data==cur.next.data:
            cur.next=cur.next.next
        else:
            cur=cur.next
    return head()
'''
Binary Search Tree
    - Hieracial Data Structute
    - left < root < right
    - Big O:
        - lookup O(log N)
        - insert O(log N)
        - delete O(log N)
    
Methods
    Initialize an empty BST Object
    Insert()
    delete()
    lookup()

'''


class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


# class BST:
#     def __init__(self, Node) -> None:


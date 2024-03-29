"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def helper( node: 'Node'):
            
            if not node:
                return None
            
            scanner = node.next
            while scanner:

                if scanner.left:
                    scanner = scanner.left
                    break

                if scanner.right:
                    scanner = scanner.right
                    break

                scanner = scanner.next

            if node.right:
                node.right.next = scanner 

            if node.left:
                node.left.next = node.right if node.right else scanner

            helper( node.right )  
            helper( node.left )  
                
            return node
        
        return helper(root)         
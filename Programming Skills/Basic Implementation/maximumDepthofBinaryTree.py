from typing import Optional
class TreeNote:
    def __init__(self, val = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right= right

class Tree:
    def maxDepth(self, root: Optional[TreeNote])->int:
        if root == None:
            return 0
    
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right)+1

# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# null is not pre-defined in Python. we use None here
n1 = TreeNote()
n2 = TreeNote()
n3 = TreeNote()
n4 = TreeNote()
n5 = TreeNote()
n1.val=3
n2.val = 9
n3.val = 20
n4.val = 15
n5.val = 7
n1.left = n2
n1.right = n3
n3.left=n4
n3.right=n5

tree = Tree()
print(tree.maxDepth(n1))

# Input: root = [1,null,2]
# Output: 2

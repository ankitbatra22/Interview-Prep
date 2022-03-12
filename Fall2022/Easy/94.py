# Understanding BST inorder traversal

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive (DFS). O(n) time and O(n) space.
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None: 
            return []
        
        def dfs(root,res):
            if root is not None:
                dfs(root.left,res)
                res.append(root.val)
                dfs(root.right,res)
            return res
        
        return dfs(root,[])

# Iterative solution using stack
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None: 
            return []
        
        res = []
        stack = []
        cur = root
        while cur is not None or len(stack) > 0:
            # go to the left most node and append all values on the way to the stack.
            while cur is not None:
                stack.append(cur)
                cur = cur.left
            # pop the last node from the stack and append its value to the result.
            print(print_stack(stack))
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right

        return res

# print stack function
def print_stack(stack):
    arr = []
    for i in range(len(stack)):
        arr.append(stack[i].val)
    return arr
  
# binary tree to test:
#         9
#       /   \
#      7    20
#     / \  /  \
#    2   8 15  22


def test_94():
    s = Solution()
    root = TreeNode(9)
    root.left = TreeNode(7)
    root.right = TreeNode(20)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(8)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(22)
    assert s.inorderTraversal(root) == [2,7,8,9,15,20,22]
    print(s.inorderTraversal(root))

test_94()
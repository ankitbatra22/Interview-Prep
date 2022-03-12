# Understanding BST preorder traversal

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# recursive solution. O(n) time and O(n) space.
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        def dfs(root, array):
            if root is not None:
                array.append(root.val)
                dfs(root.left, array)
                dfs(root.right, array)
            return array
    
        return dfs(root, [])

# iterative solution using stack. O(n) time and O(n) space.
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        res = []
        stack = []
        cur = root
        while cur is not None or len(stack) > 0:
            while cur is not None:
                print(cur.val)
                stack.append(cur)
                res.append(cur.val)
                cur = cur.left
            print(print_stack(stack))
            print("result", res)
            cur = stack.pop()
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

# test function:
def test_144():
  s = Solution()
  root = TreeNode(9)
  root.left = TreeNode(7)
  root.right = TreeNode(20)
  root.left.left = TreeNode(2)
  root.left.right = TreeNode(8)
  root.right.left = TreeNode(15)
  root.right.right = TreeNode(22)
  assert s.preorderTraversal(root) == [9, 7, 2, 8, 20, 15, 22]
  print(s.preorderTraversal(root))

test_144()
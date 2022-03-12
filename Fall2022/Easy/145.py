# Understanding BST postorder traversal

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# recursive solution. O(n) time and O(n) space.
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        def dfs(root, array):
            if root is not None:
                dfs(root.left, array)
                dfs(root.right, array)
                array.append(root.val)
            return array
        
        return dfs(root, [])


# iterative solution using stack. O(n) time and O(n) space.
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        res = []
        stack = []
        cur = root
        while cur is not None or len(stack) > 0:
            while cur is not None:
                stack.append(cur)
                res.append(cur.val)
                print("res", res)
                cur = cur.right
            cur = stack.pop()
            print(print_stack(stack))
            cur = cur.left
        
        return res[::-1]

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

# test function
def test_145():
  s = Solution()
  root = TreeNode(9)
  root.left = TreeNode(7)
  root.right = TreeNode(20)
  root.left.left = TreeNode(2)
  root.left.right = TreeNode(8)
  root.right.left = TreeNode(15)
  root.right.right = TreeNode(22)
  assert s.postorderTraversal(root) == [2, 8, 7, 15, 22, 20, 9]

test_145()
  
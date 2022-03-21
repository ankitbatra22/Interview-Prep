class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        def valid(left, right, node):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False
            return (valid(left, node.val, node.left) and 
                    valid(node.val, right, node.right))
    
        return valid(float("-inf"), float("inf"), root)


# O(n) time
# Idea is to use DFS recursively and have left and right boundries. Node val should always be between left and right for it to be valid
# Then recursively call the left and right subtree up to the left and right boundry accordingly.


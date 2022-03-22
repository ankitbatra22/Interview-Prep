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
# When going left, update right boundry to curr node val. When going right, update left boundry to curr node val.

# BST: 
#       9
#     /   \
#    7    20
#   / \  /  \
#  2   8 15  22

# -inf < 9 < inf

# -inf < 7 < 9
# -inf < 2 < 7
# -inf < 8 < 7

# 9 < 20 < inf
# 9 < 15 < 20
# 20 < 22 < inf






# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root:TreeNode) -> TreeNode:
        dummy = TreeNode(0)
        curr = dummy
        
        def inorder(inner):
            nonlocal curr
            if not inner:
             return 
            inorder(inner.left)
            curr.right = TreeNode(inner.val)
            curr = curr.right
            inorder(inner.right)
        inorder(root)

        return dummy.right
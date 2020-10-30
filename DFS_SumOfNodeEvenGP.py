#1315. Sum of Nodes with Even-Valued Grandparent
class Solution:    
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(root, parent, grandparent):
            if not root:
                return 0
                
            left, right = 0, 0
            cur = 0
            if grandparent and grandparent.val % 2 == 0:
                cur = root.val
                    
            if root.left:
                left = dfs(root.left, root, parent)
            
            if root.right:
                right = dfs(root.right, root, parent)
            
            return left + right + cur
        
        return dfs(root, None, None)
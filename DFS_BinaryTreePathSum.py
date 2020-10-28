class TreeNode:
    def __init__(self,val,left= None, right=None):
        self.val = val
        self.left,self.right = left, right

def has_path(root,sum):
    if root is None:
        return False
    
    #if current node is leaf and its value is equal to the sum, we have found a path
    if root.val == sum and root.left is None and root.right is None:
        return True
    
    #recursively call to traverse the left and right sub-tree
    #reeturn true if any of the two recursive call return true
    return has_path(root.left, sum - root.val) or has_path(root.right, sum - root.val)

'''
Time complexity #
The time complexity of the above algorithm is O(N), 
where ‘N’ is the total number of nodes in the tree. This is due to the fact that we traverse each node once.

Space complexity #
The space complexity of the above algorithm will be O(N) in the worst case. This space will be used to store the recursion stack.
The worst case will happen when the given tree is a linked list (i.e., every node has only one child).
'''
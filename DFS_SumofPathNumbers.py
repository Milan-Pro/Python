'''
Given a binary tree where each node can only have a digit (0-9) value, each root-to-leaf path will represent a number. Find the total sum of all the numbers represented by all paths.
Example:  Output: 408 Explaination: The sume of all path numbers: 17 + 192 + 199
'''
class TreeNode:
    def _init_(self,val,right=None,left=None):
        self.val =  val
        self.right = right
        self.left = left
    
def find_sum_of_path_numbers(root):
        return find_root_to_leaf_path_numbers(root,0)
    
def find_root_to_leaf_path_numbers(currentNode, pathSum):
    if currentNode is None:
        return 0
    #Calculate the path Numebr of current Node
    pathSum = 10 * pathSum + currentNode.val
    
    #if the current node is a leaf, return the current path sum
    if currentNode.left is None and currentNode.right is None:
        return pathSum
    
    #traverse left and right sub-tree
    return find_root_to_leaf_path_numbers(currentNode.left,pathSum )+ find_root_to_leaf_path_numbers(currentNode.right,pathSum)

'''
Time complexity #
The time complexity of the above algorithm is O(N), where ‘N’ is the total number of nodes in the tree. This is due to the fact that we traverse each node once.

Space complexity #
The space complexity of the above algorithm will be O(N) in the worst case. 
This space will be used to store the recursion stack. The worst case will happen when the given tree is a linked list (i.e., every node has only one child).
'''
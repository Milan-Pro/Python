'''
Given a binary tree and a number ‘S’, find all paths from root-to-leaf such that the sum of all the node values of each path equals ‘S’.
S: 12Output: 2Explaination: There are the two paths with sum '12':1 -> 7 -> 4 and 1 -> 9 -> 2 
'''
class TreeNode:
    def __init__(self,val,right=None,left=None):
        self.val = val
        self.right = right
        self.left = left

def find_path(root,sum):
    allPath = []
    find_path_recursive(root,sum,[],allPath)
    return allPath

def find_path_recursive(currentNode, sum, currentPath, allPath):
    if currentNode is None:
        return
    
    #add the current node to the path
    currentPath.append(currentNode.val)

    #if the current node is leaf and its value is euqal to sum, save the current path
    if currentNode.val == sum and currentNode.left is None and currentNode.right is None:
        allPath.append(list(currentPath))
    else:
        #traverse the left sub-tree
        find_path_recursive(currentNode.left,sum - currentNode.val,currentPath,allPath)
        #traverse the right sub-tree
        find_path_recursive(currentNode.right,sum - currentNode.val,currentPath,allPath)
    
    #remove the current node from the path to backtrack
    # we need to remove the current node while we are going up the recursive call stack.
    del currentPath[-1]
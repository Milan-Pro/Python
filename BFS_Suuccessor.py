'''
Problem Statement #
Given a binary tree and a node, find the level order successor of the given node in the tree. The level order successor is the node that appears right after the given node in the level order traversal.

Example 1:
Given Node: 3
Level Order Successor: 4
'''
from collections import deque

class TreeNode:
    def _init_(self,val):
        self.val = val
        self.right, self.left = None,None

def find_successor(self,root:TreeNode,key):
    if root is None:
        return None
    
    queue = deque()
    queue.append(root)
    while queue:
        currentNode = queue.popleft()

        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)

        if currentNode.val == key:
            break

    return queue[0] if queue else None

'''
Time complexity #
The time complexity of the above algorithm is O(N), where ‘N’ is the total number of nodes in the tree. This is due to the fact that we traverse each node once.
Space complexity #
The space complexity of the above algorithm will be O(N) as we need to return a list containing the level order traversal. 
'''
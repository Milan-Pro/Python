'''
Given a binary tree, populate an array to represent its level-by-level traversal. You should populate the values of all nodes of each level from left to right in separate sub-arrays.

Example 1:Level Order Traversal: 
  [[1],
  [2,3],
[4,5,6,7]]
'''
from collections import deque

class TreeNode:
    def _init_(self,val):
        self.val = val
        self.left,self.right = None, None

def traverse(self, root: TreeNode) -> List[int]:
    result = []
    if root is None:
        return result
    
    queue = deque()
    queue.append(root)

    while queue:
        levelSize = len(queue)
        currentLevel = []
        for _ in range(levelSize):
            currentNode = queue.popleft
            #add the node to the current level
            currentlevel.append(currentNode.val)
            #insert the childern of current Node in the queue
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
            
        result.append(currentLevel)
    
    return result

'''
Time complexity #
The time complexity of the above algorithm is O(N), where ‘N’ is the total number of nodes in the tree. This is due to the fact that we traverse each node once.

Space complexity #
The space complexity of the above algorithm will be O(N) as we need to return a list containing the level order traversal. 
We will also need O(N) space for the queue. Since we can have a maximum of N/2 nodes at any level (this could happen only at the lowest level), 
therefore we will need O(N) space to store them in the queue.

'''
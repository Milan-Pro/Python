'''
Given a binary tree, populate an array to represent the averages of all of its levels.
Example 1:
[1,2,3,4,5,6,7]
Level Averages: [1,2.5,5.5]
This problem follows the Binary Tree Level Order Traversal pattern. We can follow the same BFS approach.
The only difference will be that instead of keeping track of all nodes of a level,
 we will only track the running sum of the values of all nodes in each level. In the end, we will append the average of the current level to the result array.
'''
from collections import deque

class TreeNode:
    def _init_(self,val):
        self.val = val
        self.left,self.right = None,None

def find_level_avg(self,root: TreeNode) -> ListNode:
    result = []
    if root is None:
        return result
    
    queue = deque()
    queue.append(root)
    while queue:
        levelSize = len(queue)
        levelSum = 0.0
        for _ in range(levelSize):
            currentNode = queue.popleft()
            # add the node value to the running sum
            levelSum += currentNode.val
            #insert the children of current node to the queue
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

        #append the current level's average to the result array.    
        result.append(levelSum/levelSize)
    
    return result

'''
Time complexity #
The time complexity of the above algorithm is O(N), where ‘N’ is the total number of nodes in the tree. This is due to the fact that we traverse each node once.
Space complexity #
The space complexity of the above algorithm will be O(N) as we need to return a list containing the level order traversal. 
'''
#Similar Problems #
#Problem 1: Find the largest value on each level of a binary tree.

#Solution: We will follow a similar approach, but instead of having a running sum we will track the maximum value of each level.

#maxValue = max(maxValue, currentNode.val)


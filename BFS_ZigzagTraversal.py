'''
Problem Statement #
Given a binary tree, populate an array to represent its zigzag level order traversal. 
You should populate the values of all nodes of the first level from left to right, then right to left for the next level and keep alternating in the same manner for the following levels.
'''
from collections import deque

class TreeNode:
    def _init_(self,val):
        self.val = val
        self.left, self.right = None, None

def traverse(root):
    result = []
    if root is None:
        return result
    
    queue = deque()
    queue.append(root)
    #taking flag to identify direction
    leftToRight = True

    while queue:
        levelSize = len(queue)
        currentLevel = deque()
        for _ in range(levelSize):
            currentNode = queue.popleft
            # add node to the current level based on the traversal direction
            if leftToRight:
                currentLevel.append(currentNode.val)
            else:
                currentLevel.appendleft(currentNode.value)

            # insert the children of curent node in the queue
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
            
        result.append(list(currentLevel))
        # reverse the traversal direction by changing the flag
        leftToRight = not leftToRight

    return result

'''
Time complexity #
The time complexity of the above algorithm is O(N), where ‘N’ is the total number of nodes in the tree. This is due to the fact that we traverse each node once.
Space complexity #
The space complexity of the above algorithm will be O(N) as we need to return a list containing the level order traversal. 
'''
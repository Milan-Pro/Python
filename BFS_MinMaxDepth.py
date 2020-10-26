#Find the minimum depth of a binary tree. The minimum depth is the number of nodes along the shortest path from the root node to the nearest leaf node.
#Example 1:
# Minimum Depth:  2 / Max Depth: 3

from collections import deque
class TreeNode:
    def _init_(self,val,left=None,right=None):
        self.val = val
        self.left,self.right=left,right

def min_depth(self,root:TreeNode) -> ListNode:
    if root is None:
        return 0

    queue = deque()
    queue.append(root)
    minTreeDepth = 0

    while queue:
        minTreeDepth += 1
        levelSize = len(queue)
        for _ in range(levelSize):
            currentNode = queue.popleft()
            #Checking for the leaf node
            if not currentNode.left and not currentNode.right:
                return minTreeDepth
            #appending children of current node in to queue
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
            
def max_depth(self,root:TreeNode) -> ListNode:
    if root is None:
        return 0
    queue = deque()
    queue.append(root)
    maxTreeDepth = 0

    while queue:
        maxTreeDepth += 1
        levelSize = len(queue)
        for _ in range(levelSize):
            currentNode =  queue.popleft()

            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
            
        return maxTreeDepth

'''
Time complexity #
The time complexity of the above algorithm is O(N), where ‘N’ is the total number of nodes in the tree. This is due to the fact that we traverse each node once.
Space complexity #
The space complexity of the above algorithm will be O(N) as we need to return a list containing the level order traversal. 
'''
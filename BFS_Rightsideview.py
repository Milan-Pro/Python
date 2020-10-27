from collections import deque

class TreeNode():
    def _init_(self,val):
        self.val=val
        self.left,self.right =  None,None

def rightTraversalTree(self,root: TreeNode)->List[int]:
    result = []
    if root is None:
        return result
        
    queue = deque()
    queue.append(root)
    while queue:
        levelSize = len(queue)

        for i in range(levelSize):
            currentNode = queue.popleft()
            # if it's the rightmost element
            if i == levelSize - 1:
                result.append(currentNode.val) 
            # add child nodes in the queue 
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
    return result
'''
Time complexity: O(N) since one has to visit each node.

Space complexity:O(D) to keep the queues, where D is a tree diameter. 
'''
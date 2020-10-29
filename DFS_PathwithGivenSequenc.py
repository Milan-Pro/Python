class TreeNode:
    def _init_(self,val,right=None, left=None):
        self.val = val
        self.right, self.left = right, left
    
def find_path(root, sequence):
    if not root:
        return len(sequence) == 0

    return find_path_recursive(root,sequence,0)

def find_path_recursive(currentNode, sequence, sequenceIndex):

    if currentNode is None:
        return False
    
    seqLen = len(sequence)
    if sequenceIndex >= seqLen or currentNode.val != sequence[sequenceIndex]:
        return False
    
    if currentNode.left is None and currentNode.right is None and sequenceIndex == seqLen - 1:
        return True

    #traverse recursively left and right sub-tree
    return find_path_recursive(currentNode.left,sequence,sequenceIndex+1) or find_path_recursive(currentNode.right,sequence, sequenceIndex + 1)

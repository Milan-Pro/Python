from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        window = deque()
        
        window_maximum = []
        
        # linear scan
        for idx, number in enumerate(nums):
            
            while window and nums[ window[-1] ] < number:
                # always keep window in decreasing order as monotone queue
                window.pop()
            
            # push in new index on the right for each round of sliding towards right
            window.append(idx)
            
            if window[0] == idx - k:
                # pop out old index on the left for each round of sliding towards right
                window.popleft()
                
            
            if idx >= (k - 1):
                # output maximum element of current window
                window_maximum.append( nums[ window[0] ] )
                
        return window_maximum
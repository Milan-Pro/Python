'''
Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''

def trappingWater(self,height):
    #take Pointer
    l, r = 0, len(height) - 1
    lmax = rmax = 0
    area = 0
    # Calculate the height of the lower tower of the current tower on either side of it.
    while l < r:
        if height[l] < height[r]:
            if lmax > height[l]:
                lmax = height[l]
            else:
                 # Calculate the water stored on top of every tower
                area += lmax - height[l]
            l += 1
        else:
            if rmax > height[r]:
                rmax = height[r]
            else:
                area += rmax - height[r]
            r -= 1
    return area 

'''
Time complexity: O(n). Single iteration of O(n).
Space complexity: O(1) extra space. Only constant space required for left, right,left_max and right_max.
'''
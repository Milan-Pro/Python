# Two Pointer approach
# target sum indices
def target_pair(arr, target_sum):
    left, right = 0, len(target_sum) - 1
    
    while left < right:
        #calculate sum at pointer Left and right
        currentSum = arr[left] + arr[right]
        if currentSum == target_sum:
            return [left,right]
        
        #if current sum < target then increase left pointer
        if target_sum > currentSum:
            left += 1
        # otherwise increment right pointer
        else:
            right -= 1
    return [-1,-1]

'''
Time Complexity #
The time complexity of the above algorithm will be O(N), where ‘N’ is the total number of elements in the given array.

Space Complexity #
The algorithm runs in constant space O(1).
'''
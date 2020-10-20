# Two Pointer approach
# target sum indices
def target_pair(arr, target_sum):
    left, right = 0, len(arr) -1
    while left < right :
        curr_sum = arr[left] + arr[right]
        if curr_sum == target_sum:
            return [left,right]
        
        if target_sum > curr_sum:
            left += 1
        else:
            right -= 1
        return [-1,-1]

import math
def smallest_Subarray_with_Sum(arr,S):
    # Taking Start of sliding window and initial window sum with min_length
    window_sum = 0
    window_start = 0
    min_length = math.inf

    for window_end in range(0,len(arr)): # taking window end and creating slidin window
        window_sum += arr[window_end]    # adding eliment of sliding window

        while window_sum >= S: #Checking for Sum
            min_length = min(min_length, window_end - window_start + 1) # Keeping track of minimun sliding window length
            window_sum -= arr[window_start] # shrinking sliding window from start
            window_start += 1 # incrementing sliding window by one
    if min_length == math.inf:
        return 0
    return min_length

    # Time complexity O(N + N) = O(N) Outer for loop running for all element and inner while loop running for each element only once.  
    # Space complexity o(1)
    
def main():
    print("Smallest Subarray length:" + str(smallest_Subarray_with_Sum([3, 4, 1, 1, 6],8)))
    print("Smallest Subarray length:" + str(smallest_Subarray_with_Sum([2, 1, 5, 2, 3, 2],7)))
    print("Smallest Subarray length:" + str(smallest_Subarray_with_Sum([2, 1, 5, 2, 8],7)))
main()
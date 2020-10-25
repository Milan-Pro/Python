'''
Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
#Approach1: 
Brute Force approach is two loop outer loop will go for the each number and inner loop will do the sum for i+k till we find the sum.
this will take O(n*k) time

#Approach 2: Fix sliding Window
Move the sliding window based on our requiremnt 
1) Subtract the element going out of the sliding window i.e., subtract the first element of the window.
2) Add the new element getting included in the sliding window i.e., the element coming right after the end of the window.

O(N)
'''
def max_sub_aaray_of_size_k(arr,k):
    max_sum, window_sum = 0,0
    window_start = 0


    for window_end in range(len(arr)):
        window_sum += arr[window_end] # add the next element
        #slide the window, we don't need to slide if we have not hit the require window size of 'k'
        if window_end >= k-1:
            max_sum = max(max_sum,window_sum)
            window_sum -= arr[window_start] # subtract the elemnt going out
            window_start += 1 # move the window towards the next
    return max_sum

def main():
    print("Max if sub array of size k"+ str(max_sub_aaray_of_size_k(2,[2,3,4,1,5])))

main()
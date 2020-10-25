##### Brute Force #######

def find_avg_ofarray(K, arr):
    result = []
    for i in range(len(arr) - K + 1):
        sum = 0.0
        for j in range(i, i+K):
            sum += arr[j]
        result.append(sum/K)
    return result

# Time space is O(n * k)

##### Optimised Approach ########
def find_avg_ofarray1(K, arr):
    result = []
    window_start = 0
    window_Sum = 0.0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd] # add the next element
        # slide the window, we don't need to alide if we have not hit the required window size of 'k'
        if windowEnd >= K - 1:
            result.append(windowSum / K) # Calculate the Average
            windowSum -= arr[windowStart] # remove element going out
            windowStart += 1 # slide the windw by 1
    return result

# Time Space is O(n)
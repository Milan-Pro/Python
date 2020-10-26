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
    for window_End in range(len(arr)):
        window_Sum += arr[window_End] # add the next element
        # slide the window, we don't need to alide if we have not hit the required window size of 'k'
        if window_End >= K - 1:
            result.append(window_End / K) # Calculate the Average
            window_Sum -= arr[window_start] # remove element going out
            window_start += 1 # slide the windw by 1
    return result

# Time Space is O(n)
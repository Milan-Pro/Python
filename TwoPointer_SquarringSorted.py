'''
Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.
Example 1:
Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]
'''
def squarringsortes(arr):
    n = len(arr)
    #Lets take pointer
    left,right = 0, len(arr) - 1
    #this is to change the order
    highestSortedIndex = n - 1
    squaredArr = [0 for x in len(n)]


    while left < right:
        #Count left square and right square
        leftsquare = arr[left] * arr[left]
        rightsquare = arr[right] * arr[right]
        #changing index or sorting based on square value
        if leftsquare > rightsquare:
            squaredArr[highestSortedIndex] = leftsquare
            left += 1 # incrementing left
        else:
            squaredArr[highestSortedIndex] = rightsquare
            right -= 1 # incrementing right
        highestSortedIndex -= 1 

    return squaredArr
'''
Time complexity #
The time complexity of the above algorithm will be O(N) as we are iterating the input array only once.

Space complexity #
The space complexity of the above algorithm will also be O(N); this space will be used for the output array.
'''


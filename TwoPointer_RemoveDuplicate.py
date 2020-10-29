'''
Problem Statement #
Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in-place return the new length of the array.

Example 1:
Input: [2, 3, 3, 3, 6, 9, 9] Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].
'''
def remove_duplicate(arr):
    next_nonduplicate = 1

    i = 1
    while i < len(arr):
        if arr[next_nonduplicate - 1] != arr[i]:
            arr[next_nonduplicate] = arr[i]
            next_nonduplicate += 1
        i += 1
    
    return next_nonduplicate

'''
Time: O(N)
Space: O(1)
'''
'''
Similar Questions #
Problem 1: Given an unsorted array of numbers and a target ‘key’, remove all instances of ‘key’ in-place and return the new length of the array.

Example 1:
Input: [3, 2, 3, 6, 3, 10, 9, 3], Key=3  Output: 4
Explanation: The first four elements after removing every 'Key' will be [2, 6, 10, 9].
'''

def remove_duplicate_nonsorted(arr,key):
    nextElement = 0
    for i in range(len(arr)):
        if arr[i] != key:
            arr[nextElement] = arr[i]
            nextElement += 1
    return nextElement

'''
Given a string, find the length of the longest substring in it with no more than K distinct characters
Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".
Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".
Solution:
->fisrt we will add char in charfreq HashMap
->then We will expand window by adding element at window_end
->once we reach greater then k then shrink the window by removing element from start
'''
def longest_substring_with_k_dist(str,k):
    window_start = 0
    max_length = 0
    char_freq = {}

    # in the following loop we'll try to expand[window_start,window_end]
    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char not in char_freq:
            char_freq[right_char] = 0
        char_freq[right_char] += 1

        # Shrink the sliding window, untill we are left with 'k' disctinct char in the char_freq
        while len(char_freq) > k:
            left_char = str[window_start]
            char_freq[left_char] -= 1
            if char_freq[left_char] == 0:
                del char_freq[left_char]
            window_start += 1 # shrink the window
        # remember the maximum length so far
        max_length = max(max_length, window_end - window_start + 1)
    return max_length

'''
Time Complexity #
The time complexity of the above algorithm will be O(N) where ‘N’ is the number of characters in the input string.
The outer for loop runs for all characters and the inner while loop processes each character only once, 
therefore the time complexity of the algorithm will be O(N+N) which is asymptotically equivalent to O(N).

Space Complexity #
The space complexity of the algorithm is O(K)O(K), as we will be storing a maximum of ‘K+1’ characters in the HashMap.
'''
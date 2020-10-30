class solution:
    def longestPalindorme(self,s:str):
        res = ""
        for i in range(len(s)):
            # odd case, like "aba"
            temp = self.helper(s,i,i)
            if len(temp) > len(res):
                res = temp
            # even case, like "abba"
            temp = self.helper(s,i,i+1)
            if len(temp) > len(res):
                res = temp
        return res
    # get the longest palindrome, l, r are the middle indexes   
    # from inner to outer
    def helper(self,s,l,r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return (s[l+1:r])
'''
Time:O(n2) since outer loop is running for every element and helper will be running either for odd or for even.
space:O(1)
'''
class solution:
    def merge_sorted(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # two get pointers for num1 and num2
        p1 = m - 1
        p2 = n - 1
        # set pointer for num1
        p = m + n - 1

        # while there are still elements to compare
        while p1 >= 0 and p2>=0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] =  nums1[p1]
                p1 -= 1
            p -= 1
        
        # add missing elements from nums2
        nums1[:p2 + 1] = nums2[:p2 + 1]
'''
Complexity Analysis

Time complexity : O(n+m).
Space complexity : O(1).
'''

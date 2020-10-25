'''
There are multiple approach to check the inersection of Two linked list
A) The Brute force
Iterate trhough LL A with length M and Iterate through LL B with length N.
 The overall time complexity is O(M*N)
(B)  ## APPROACH : 2 POINTER ##
        
        ## LOGIC ##
        # 1) Find the length of both lists;
        # 2) In the biggest list, advance its head N times where N is the length difference between the two lists.
        # 3) Now both lists have the same length, just iterate them and check for node equality.
        
		## TIME COMPLEXITY : O(M+N) ##
		## SPACE COMPLEXITY : O(1) ##
'''
class ListNode:
    def _init_(self,value, next = None):
        self.next = next
        self.value = value
class Solution:
    def getIntersection(self, headA:ListNode, headB:ListNode)-> ListNode:
        la = lb = 0
        m, n = headA, headB

        #Find the length of both lists
        while(headA):
            la += 1
            headA = headA.next
        while(headB):
            lb += 1
            headB = headB.next
        
        # 2) In the biggest list, advance its head N times where N is the length difference between the two lists.
        if(la > lb):
            diff = la - lb
            while(diff):
                m = m.next
                diff -= 1
        else:
            diff = lb - la
            while(diff):
                n= n.next
                diff -= 1
        
        # 3) Now both lists have the same length, just iterate them and check for node equality.
        while( m and n):
            if(m == n): return m
            m = m.next
            n = n.next
        return None
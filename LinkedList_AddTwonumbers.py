class ListNode:
    def _init_(self,value,next= None):
        self.value = value
        self.next = next
#Approach 1
class Solution2:
    def addTwoNumbers2(self, l1: ListNode, l2: ListNode,c = 0) -> ListNode:
        
        val = l1.val + l2.val + c
        c = val // 10
        ret = ListNode(val % 10 ) 
        
        if (l1.next != None or l2.next != None or c != 0):
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            ret.next = self.addTwoNumbers2(l1.next,l2.next,c)
        return ret

#Approach 2
class Solution:
    def addTwoNumber(self, l1: ListNode, l2: ListNode) -> ListNode :
        result = ListNode(0)
        l3 = result
        carry = 0

        while l1 or l2 or carry:
            currentSum = 0
            currentSum += carry

            if l1:
                currentSum += l1.value
            if l2:
                currentSum += l2.value
            
            digit = currentSum % 10
            carry = currentSum // 10

            l3.val = digit
            if l1 or l2 or carry:
                l3.next = ListNode(0)
                l3 = l3.next
        return result


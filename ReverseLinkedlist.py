class ListNode:
    def _init_(self,val,next=None):
        self.value = val
        self.next = next

class solution:
    def reverse_linkedlist(self,head: ListNode) -> ListNode:
        prev, cur, next = None, head, None

        while cur != None:
            next = cur.next # temporary store next node
            cur.next = prev # reverse the current next (current.next pointer chnage to prev) 
            prev = cur      # before we move to next node, point prev to current node
            cur = next      # move to the next node
        return prev

'''
Time: O(n)
Space: O(1)
0 <- 1 <- 2 <- 3 -> 4 -> 5
           c    
              n     
        p
https://www.youtube.com/watch?v=TSDl7sRxWdU
'''
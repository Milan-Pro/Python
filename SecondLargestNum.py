#Find the second largest nmber in the array
class solution:
    def secondLargest(self,L) -> int:
        s=[]
        for num in sorted(L):
            if len(s) > 0 and s[-1] == num:
                continue
            s.append(num) 

#SecondApproach

def second_largest(self,L:list):
    maxVal = -float('inf')
    for num in L:
        maxVal = max(maxVal,num)
    print (maxVal)
    secondMax = -float('inf')
    for num in L:
        if num == maxVal:
            continue
        secondMax = max(secondMax,num)
    print (secondMax)
L = [5, 9, 2, 2, 2, 7, 8, 9, 9]

second_largest([5, 9, 2, 2, 2, 7, 8, 9, 9])

secondLargest([5, 9, 2, 2, 2, 7, 8, 9, 9])
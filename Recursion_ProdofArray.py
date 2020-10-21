#Given an array of integers, Replace each element with the product of the rmaining elements.
# input: {1,2,3,4,5}
#output: {120,60,40,30,24}
#Brute force approach

def prod_array(arr):
    result = []    
    for i in range(len(arr)):
        prod = 1
        for j in range(len(arr)):
            if i != j:
                prod = prod * arr[j]
        result += [prod]    
    print (result)
    return result

arr = [1,2,3,4,5]
prod_array(arr)


def rec_Prodarr(arr, prodleft, index):
    #Termination Condition
    if index >= len(arr):
        return 1
    
    currentValue = arr[index]
    productTillcurrentIndex = currentValue * prodleft

    productOfElementRightOfCurrentIndex = rec_Prodarr(arr, productTillcurrentIndex, index+1)

    arr[index] = prodleft * productOfElementRightOfCurrentIndex

    return currentValue * productOfElementRightOfCurrentIndex
    print (productOfElementRightOfCurrentIndex)


arr = [1,2,3,4,5]
rec_Prodarr(arr, 1, 0)
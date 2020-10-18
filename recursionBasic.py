# Get max eliment of an array using recursion (Non Tail recursive)
arr = [12,23,34,45]
n = len(arr)
def getMax(arr,n):
    if n  == 1:                     #### End Conditioon ####
        return arr[0]               #### End Conditioon ####
    
    max_val = getMax(arr, n - 1)    #### Recursive Step ####

    #print(max(arr[n-1],max_val))
    return max(arr[n-1],max_val)    #### Logic ####

getMax(arr, n)
    
# Print the array in reverse order (Tail Recurvsive)
def rev_Order(arr,n):
    if(n == 0): return arr[0]   #### End Conditioon ####

    print (arr[n-1], end = " ") #### Logic ####
    
    rev_Order(arr,n-1)          #### Recursive Step ####
    

arr = [12,23,34]
n = len(arr)    
rev_Order(arr,n)

# Find the reverse string using recursion
def reverseStr(string):
    if len(string) == 0: 
        return string 
    else: 
        return reverseStr(string[1:]) + string[0] 

string ="Hello Milan"
print ("The original string  is : ",end="") 
print (string) 
  
print ("The reversed string(using recursion) is : ",end="") 
print (reverseStr(string)) 

## Find string length using recursion
str ="Hello Milan"
def string_length(str) : 
      
    # if we reach at the 
    # end of the string 
    if str == '': 
        return 0
    else : 
        return 1 + string_length(str[1:])  
      
# Driver Code 
print (string_length(str)) 
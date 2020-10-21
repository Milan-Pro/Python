def longestCommonPrefix(self,strs: List[strs]) -> strs:
    # end condition if we do not have char
    if not strs:            
        return ''
    
    # find min and max length word from string List
    m, M = min(strs), max(strs)

    #enumerate min word this will give index and letter(0:m,1:i,2:l,3:a)
    for i, letters in enumerate(m):
        if letter != M[i]  # Compare char with Max word char and if that is not equal then 
            return m[:i] # return min strs word starting with 0 index to i index, 
        return m
    
    



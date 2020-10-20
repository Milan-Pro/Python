def Tower_of_Hanoi(n, s, d, a):
    if n == 1:
        print ("Move Disk 1 from source",s,"to destination",d)   #### End Condition ####
        return 

    Tower_of_Hanoi(n-1,s,a,d)                                    ### Logic and Recursion ###
    print ("Move disk",n,"from source",s,"to destination",d)     ### Logic and Recursion ###   
    Tower_of_Hanoi(n-1,a,d,s)

# Driver code 
n = 4
Tower_of_Hanoi(n,'A','B','C')  
# A, C, B are the name of rods 
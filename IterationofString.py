# Python program to iterate over characters of a string 
  
# Code #1 
string_name = "geeksforgeeks"
  
# Iterate over the string 
for element in string_name: 
    print(element, end=' ') 
print("\n") 
  
  
# Code #2 
string_name = "GEEKS"
  
# Iterate over index 
for element in range(0, len(string_name)): 
    print(string_name[element]) 

# Python program to iterate over characters of a string 

for element in string_name[ : :-1]: 
    print(element, end =' ') 
print('\n') 
  
# Code #2 
string_name = "geeksforgeeks"
  
# Getting length of string 
ran = len(string_name) 
  
# using reversed() function 
for element in reversed(range(0, ran)): 
    print(string_name[element]) 

# string_name[start:end:step] 
for element in string_name[0:8:1]:  
    print(element, end =' ') 
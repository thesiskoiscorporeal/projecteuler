'''FROM NOW ON IF YOU HAVE TO COUNT PERMUTATIONS: JUST SORT THE DIGITS TO GET A HASH(?) AND CHECK FOR NUMBER OF OCCURENCES'''

list_of_cubes = [x**3 for x in range(10000)]

NO_OF_CHARS = 256
def arePermutation(str1, str2): 
  
    # Create two count arrays and initialize 
    # all values as 0 
    count1 = [0] * NO_OF_CHARS 
    count2 = [0] * NO_OF_CHARS 
  
    # For each character in input strings, 
    # increment count in the corresponding 
    # count array 
    for i in str1: 
        count1[ord(i)]+=1
  
    for i in str2: 
        count2[ord(i)]+=1
  
    # If both strings are of different length. 
    # Removing this condition will make the  
    # program fail for strings like 
    # "aaca" and "aca" 
    if len(str1) != len(str2): 
        return 0
  
    # Compare count arrays 
    for i in range(NO_OF_CHARS): 
        if count1[i] != count2[i]: 
            return 0
  
    return 1


for j in range(345, len(list_of_cubes)):
    match_count = 0 #set match count to 0
    for k in range(j, len(list_of_cubes)):
        if arePermutation(str(list_of_cubes[j]),str(list_of_cubes[k])) == True:
            match_count += 1 #increment match count if match found
        if len(str(list_of_cubes[j])) != len(str(list_of_cubes[k])):
            break
        
    if match_count == 5: #because of self match
        print(j)
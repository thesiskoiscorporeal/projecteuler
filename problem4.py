def reverse(s): 
    return s[::-1] 
  
def isPalindrome(s): 
    # Calling reverse function 
    rev = reverse(s) 
  
    # Checking if both string are equal or not 
    if (s == rev): 
        return True
    return False

largest = 0

for a in range(1000):
    for b in range (1000):
        if isPalindrome(str(a*b)) and a*b>largest:
            largest = a*b

print(largest)
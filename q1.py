def longest_palindromic_substring(s):
    """
    Given a string find the longest palindromic substring
    """
    longest = ""
    n = len(s)
    
   
    for i in range(n):
        
        for j in range(i + 2, n + 1): 
            
            substring = s[i:j]
            
            if  substring == substring[::-1]:
                
                if len(substring)>len(longest):
                    longest = substring
    
    return longest
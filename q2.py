def remove_adjacent_duplicates(s):
    '''
    Given a string remove all the adjacent duplicate characters and return the string
    '''
    found_duplicate = True
    
    while found_duplicate:
        
        found_duplicate = False
        
        for i in range(len(s) - 1):
            
            if s[i] == s[i+1]:
               
                s = s[:i] + s[i+2:]
                
                found_duplicate = True
                
                break 
    return s
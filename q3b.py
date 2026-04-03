def add_binary(a, b):
    '''
    Given two strings perform binary addition and return the result as a string
    '''
    s1 = a[2:]
    s2 = b[2:]
    
    result = ""
    carry = 0
    
    i = len(s1) - 1
    j = len(s2) - 1
    
    
    while i >= 0 or j >= 0 or carry:
       
        val1 = 1 if (i >= 0 and s1[i] == '1') else 0
        val2 = 1 if (j >= 0 and s2[j] == '1') else 0
        
        total = val1 + val2 + carry
        carry = total // 2
        bit = total % 2
        
        
        if bit == 1:
            result = "1" + result
        else:
            result = "0" + result
            
        i -= 1
        j -= 1

    
    start_index = -1
    for k in range(len(result)):
        if result[k] == '1':
            start_index = k
            break
    
    
    if start_index == -1:
        return "0b0"
    
    
    return "0b" + result[start_index:]
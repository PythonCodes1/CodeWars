# Adding 2 arrays full of integers

def array_plus_array(arr1,arr2):
    sum=0
    sum1=0
    for i in range(0, len(arr1)):
        sum = sum + arr1[i]; 
    
    for i in range(0, len(arr2)):
        sum1 = sum1 + arr2[i];  
        
    return sum + sum1
    pass

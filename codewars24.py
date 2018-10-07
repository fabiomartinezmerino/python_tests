def max_product(lst, n_largest_elements):
    """
    input: lst the number of items of array that is function is to multiply
    and return
    
    input: n_largest_elements is the list of numbers that will be sorted
    and then its lst largest elements will be multiplied and returned
    
    return: multiplied_list is a number obtained multiplying the lst largest
    numbers of the array 
    """
    
    #first we sort the array in reverse order
    
    n_largest_elements = sorted(n_largest_elements,reverse=True)
    
    #now we iterate through the list multiplying first lst numbers
    
    counter = 0
    max_product = 1
    while counter < lst:
        max_product *= n_largest_elements[counter]
        counter +=1
   
    return max_product
    
print(max_product(2,[2,3,4,3,2,1,5]))
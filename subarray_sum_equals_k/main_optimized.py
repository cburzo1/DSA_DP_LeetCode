def subarray_sum_equals_k(arr, k):
    count = 0

    '''
    [1,1,1]
     0 1 2    
    [0, 1, 1] -> rl = 2
     0 1 2
     
     [1,2,3]
     0 1 2    
    [0, 1, 1] -> rl = 2
     0 1 2
    '''

    return count

print("RET: ", subarray_sum_equals_k([1, 1, 1], 2))
print("RET: ", subarray_sum_equals_k([1, 2, 3], 3))
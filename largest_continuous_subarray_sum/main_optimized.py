def largest_continous_subarray_optimized(arr):

    max_sum = arr[0]
    current_sum = 0

    for i in range(0, len(arr)):
        current_sum = current_sum + arr[i]
        if current_sum > max_sum:
            max_sum = current_sum

        if current_sum < 0:
            current_sum = 0

    return max_sum
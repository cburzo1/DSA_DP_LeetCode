def subarray_sum_equals_k(arr, k):
    count = 0

    for i in range(len(arr)):
        current_sum = 0
        for j in range(i, len(arr)):
            current_sum += arr[j]
            if current_sum == k:
                count += 1

    return count

print("RET: ", subarray_sum_equals_k([1, 1, 1], 2))
print("RET: ", subarray_sum_equals_k([1, 2, 3], 3))
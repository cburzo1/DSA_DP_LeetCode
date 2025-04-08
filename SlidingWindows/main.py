class Solution(object):
    def findMaxAverage(self, nums, k):
        arr = []
        j = k

        for i in range(0, len(nums)):
            tot = 0
            avg = 0
            while i < k:
                tot = tot + nums[i]
                i = i + 1

            avg = tot/j
            arr.append(avg)

            if k == len(nums):
                break
            else:
                k = k + 1

        max = 0

        for i in range(0, len(arr)):
            if arr[i] > max:
                max = arr[i]

        return max

solution = Solution()

print(solution.findMaxAverage([5], 1))
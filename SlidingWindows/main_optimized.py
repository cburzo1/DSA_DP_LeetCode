class Solution(object):
    def findMaxAverage(self, nums, k):
        tot = 0

        for i in range(k):
            tot = tot + nums[i]

        max_avg = float(tot)/float(k)

        for i in range(k, len(nums)):
            tot = tot + nums[i]
            tot = tot - nums[i-k]

            avg = float(tot)/float(k)
            max_avg = max(max_avg, avg)

        return max_avg

solution = Solution()

print(solution.findMaxAverage([5], 1))
class Solution(object):
    def twoSum(self, numbers, target):
        idx1 = 0
        idx2 = len(numbers) - 1

        while idx1 < idx2:
            if numbers[idx1] + numbers[idx2] > target:
                idx2 = idx2 - 1

            elif numbers[idx1] + numbers[idx2] < target:
                idx1 = idx1 + 1

            else:
                return [idx1, idx2]

solution = Solution()

print(solution.twoSum([-1,0,2, 3,4,7,11,15], 6))
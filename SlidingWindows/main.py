class Solution(object):
    def findMaxAverage(self, nums, k):
        arr = []

        for i in range(1, len(nums)):
            #print(i)
            tot = 0
            avg = 0
            if i + k - 1 == len(nums):
                break
            else:
                j = i
                while j <= k:
                    #print(nums[j])
                    tot = tot + nums[j]
                    j = j + 1

          #print(tot)
            avg = tot/k
            #print(avg)
            arr.append(avg)

        max = 0

        print(arr)

        for i in range(0, len(arr)):
            if arr[i] > max:
                max = arr[i]

        return max

solution = Solution()

print(solution.findMaxAverage([1,12,-5,-6,50,3], 4))
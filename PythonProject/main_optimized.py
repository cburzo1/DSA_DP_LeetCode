class NumArray(object):

    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, left, right):
        #print(self.nums, left, right)
        total = 0
        for i in range(left, right + 1):
            total = total + self.nums[i]

        return total

nA = NumArray([-2, 0, 3, -5, 2, -1])

nA.sumRange(0, 2)
nA.sumRange(2, 5)
nA.sumRange(0, 5)
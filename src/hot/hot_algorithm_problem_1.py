"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

你可以按任意顺序返回答案。
示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]

提示：

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
只会存在一个有效答案


进阶：你可以想出一个时间复杂度小于 O(n2) 的算法吗？
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # 暴力求解
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return []

        # 排序 + 双指针法（时间复杂度 $O(n \log n)$）
        # 附带原始下标：[(数值, 原始下标)]
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        # 按照数值升序排序，时间复杂度 O(n log n)
        indexed_nums.sort(key=lambda x: x[0])

        # 获取左右两个的序号下标，计算和，进行偏移
        # left, right = 0, len(nums) - 1
        # while left < right:
        #     current_sum = indexed_nums[left][0] + indexed_nums[right][0]
        #     if current_sum == target:
        #         return [indexed_nums[left][1], indexed_nums[right][1]]
        #     elif current_sum < target:
        #         left += 1
        #     else:
        #         right -= 1
        #
        # return []

        # 哈希表法 n
        hashmap = {}  # 记录 value -> index
        for i, num in enumerate(nums):
            # 获取值和下标，获取缺少的值
            complement = target - num
            # 如果缺少的值在hash中，返回数据，如果不是的话，就在hash记录下
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i
        return []


if __name__ == '__main__':
    re = Solution().twoSum([3, 2, 4], 6)
    print(re)

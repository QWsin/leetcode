#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start


class Solution:
    def twoSum(self, nums, t: int):
        mp = {}
        n = len(nums)
        for i in range(0, n):
            if mp.get(t - nums[i]) is not None:
                return [mp.get(t - nums[i]), i]
            mp[nums[i]] = i
        return [-1, 1]


# def main():
#     sol = Solution()
#     print(sol.solve([2, 7, 11, 15], 9))


# if __name__ == '__main__':
#     main()
# @lc code=end

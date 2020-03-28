#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
# https://leetcode-cn.com/problems/reverse-integer/description/
#
# algorithms
# Easy (33.63%)
# Likes:    1686
# Dislikes: 0
# Total Accepted:    276.5K
# Total Submissions: 821.9K
# Testcase Example:  '123'
#
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
#
# 示例 1:
#
# 输入: 123
# 输出: 321
#
#
# 示例 2:
#
# 输入: -123
# 输出: -321
#
#
# 示例 3:
#
# 输入: 120
# 输出: 21
#
#
# 注意:
#
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
#
#

# @lc code=start


class Solution:
    def reverse(self, x: int) -> int:
        f = 1
        if x < 0:
            f = -1
            x = -x
        num = []
        sz = 0
        while x > 0:
            num.append(x % 10)
            x //= 10
            sz += 1
        ans = 0
        for i in range(0, sz):
            ans = ans * 10 + num[i]
        if f == -1:
            ans *= -1
        if ans >= -2**31 and ans <= 2**31 - 1:
            return ans
        else:
            return 0

# @lc code=end

#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#
# https://leetcode-cn.com/problems/implement-strstr/description/
#
# algorithms
# Easy (39.51%)
# Likes:    364
# Dislikes: 0
# Total Accepted:    128.5K
# Total Submissions: 325.2K
# Testcase Example:  '"hello"\n"ll"'
#
# 实现 strStr() 函数。
#
# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置
# (从0开始)。如果不存在，则返回  -1。
#
# 示例 1:
#
# 输入: haystack = "hello", needle = "ll"
# 输出: 2
#
#
# 示例 2:
#
# 输入: haystack = "aaaaa", needle = "bba"
# 输出: -1
#
#
# 说明:
#
# 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
#
# 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
#
#

# @lc code=start


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        if len(haystack) == 0:
            return -1
        f = [-1]
        p = -1
        n = len(needle)
        for i in range(1, len(needle)):
            while p != -1 and needle[p + 1] != needle[i]: p=f[p]
            if needle[p + 1] == needle[i]: p += 1
            f.append(p)

        p = -1
        for i in range(len(haystack)):
            while p != -1 and haystack[i] != needle[p + 1]: p=f[p]
            if haystack[i] == needle[p + 1]: p += 1
            if p == n - 1: return i - n + 1
        return -1

# @lc code=end


def main():
    sol = Solution()
    print(sol.strStr("",""))


if __name__ == '__main__':
    main()

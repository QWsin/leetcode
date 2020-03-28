#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (36.14%)
# Likes:    883
# Dislikes: 0
# Total Accepted:    187.8K
# Total Submissions: 519.1K
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
#
#
# 示例 2:
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
#
#
# 说明:
#
# 所有输入只包含小写字母 a-z 。
#
#

# @lc code=start


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ''
        n = len(strs)
        if n == 0:
            return ''
        lens = []
        for i in range(n):
            lens.append(len(strs[i]))
        i = 0
        while 1:
            ok = True
            for j in range(n):
                if i >= lens[j] or strs[j][i] != strs[0][i]:
                    # print(strs[j][i], strs[0][i])
                    ok = False
                    break
            if ok is False:
                return pre
            pre += (strs[0][i])
            i += 1
        pass
# @lc code=end

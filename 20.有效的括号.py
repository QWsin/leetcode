#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
# https://leetcode-cn.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (40.85%)
# Likes:    1385
# Dislikes: 0
# Total Accepted:    204.3K
# Total Submissions: 500K
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
# 有效字符串需满足：
#
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
#
#
# 注意空字符串可被认为是有效字符串。
#
# 示例 1:
#
# 输入: "()"
# 输出: true
#
#
# 示例 2:
#
# 输入: "()[]{}"
# 输出: true
#
#
# 示例 3:
#
# 输入: "(]"
# 输出: false
#
#
# 示例 4:
#
# 输入: "([)]"
# 输出: false
#
#
# 示例 5:
#
# 输入: "{[]}"
# 输出: true
#
#

# @lc code=start


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        val = {'(': 1, '[': 2, '{': 3, ')': -1, ']': -2, '}': -3}
        for i in range(len(s)):
            if val[s[i]] > 0:
                stack.append(val[s[i]])
            else:
                if len(stack) != 0 and stack[-1] + val[s[i]] == 0:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
# @lc code=end

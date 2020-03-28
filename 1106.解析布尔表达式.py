#
# @lc app=leetcode.cn id=1106 lang=python3
#
# [1106] 解析布尔表达�?
#
# https://leetcode-cn.com/problems/parsing-a-boolean-expression/description/
#
# algorithms
# Hard (54.04%)
# Likes:    19
# Dislikes: 0
# Total Accepted:    1.6K
# Total Submissions: 3K
# Testcase Example:  '"!(f)"'
#
# 给你一�?以字符串形式表述的 布尔表达式（boolean�? expression，返回�?�式的运算结果�?
#
# 有效的表达式需遵循以下约定�?
#
#
# "t"，运算结果为 True
# "f"，运算结果为 False
# "!(expr)"，运算过程为对内部表达式 expr 进�?�逻辑 非的运算（NOT�?
# "&(expr1,expr2,...)"，运算过程为�? 2 �?或以上内部表达式 expr1, expr2, ... 进�?�逻辑 与的运算（AND�?
# "|(expr1,expr2,...)"，运算过程为�? 2 �?或以上内部表达式 expr1, expr2, ... 进�?�逻辑 或的运算（OR�?
#
#
#
#
# 示例 1�?
#
# 输入：expression = "!(f)"
# 输出：true
#
#
# 示例 2�?
#
# 输入：expression = "|(f,t)"
# 输出：true
#
#
# 示例 3�?
#
# 输入：expression = "&(t,f)"
# 输出：false
#
#
# 示例 4�?
#
# 输入：expression = "|(&(t,f,t),!(t))"
# 输出：false
#
#
#
#
# 提示�?
#
#
# 1 <= expression.length <= 20000
# expression[i] �? {'(', ')', '&', '|', '!', 't', 'f', ','} �?的字符组成�?
# expression �?以上述形式给出的有效表达式，表示一�?布尔值�?
#
#
#

# @lc code=start


def value(expression: str, l: int, r: int) -> bool:
    print(l, r)
    if r == l:
        if expression[l] == 't':
            return True
        else:
            return False
    pre = l + 1
    ans = False
    if expression[l] == '&':
        ans = True

    cnt = 0
    for i in range(l+2, r+1):
        if expression[i] == '(':
            cnt += 1
        if expression[i] == ')' and i != r:
            cnt -= 1
        if cnt == 0 and (expression[i] == ',' or i == r):
            cur = value(expression, pre + 1, i - 1)
            if expression[l] == '!':
                return not cur
            if expression[l] == '&':
                ans &= cur
                if ans is False:
                    return False
            if expression[l] == '|':
                ans |= cur
                if ans is True:
                    return True
            pre = i
    return ans


class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        n = len(expression)
        return value(expression, 0, n-1)


# def main():
#     s = "|(&(t,f,t),!(t))"
#     sol = Solution()
#     print(sol.parseBoolExpr(s))


# if __name__ == '__main__':
#     main()

# @lc code=end

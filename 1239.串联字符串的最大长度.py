#
# @lc app=leetcode.cn id=1239 lang=python3
#
# [1239] 串联字符串的最大长度
#
# https://leetcode-cn.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/description/
#
# algorithms
# Medium (37.27%)
# Likes:    25
# Dislikes: 0
# Total Accepted:    4.9K
# Total Submissions: 13.2K
# Testcase Example:  '["un","iq","ue"]'
#
# 给定一个字符串数组 arr，字符串 s 是将 arr 某一子序列字符串连接所得的字符串，如果 s 中的每一个字符都只出现过一次，那么它就是一个可行解。
#
# 请返回所有可行解 s 中最长长度。
#
#
#
# 示例 1：
#
# 输入：arr = ["un","iq","ue"]
# 输出：4
# 解释：所有可能的串联组合是 "","un","iq","ue","uniq" 和 "ique"，最大长度为 4。
#
#
# 示例 2：
#
# 输入：arr = ["cha","r","act","ers"]
# 输出：6
# 解释：可能的解答有 "chaers" 和 "acters"。
#
#
# 示例 3：
#
# 输入：arr = ["abcdefghijklmnopqrstuvwxyz"]
# 输出：26
#
#
#
#
# 提示：
#
#
# 1 <= arr.length <= 16
# 1 <= arr[i].length <= 26
# arr[i] 中只含有小写英文字母
#
#
#

# @lc code=start


class Solution:
    n = 0
    st = []
    sl = []
    ok = []

    def __init__(self):
        super().__init__()
        Solution.n = 0
        Solution.st = []
        Solution.sl = []
        Solution.ok = []

    def dfs(self, pos, arr, vis: set) -> int:
        ans = 0
        for i in range(pos+1, Solution.n):
            if (not (Solution.st[i] & vis)) and Solution.ok[i]:
                ans = max(ans, Solution.dfs(self, i, arr, vis | Solution.st[i]) + Solution.sl[i])
        return ans

    def maxLength(self, arr) -> int:
        Solution.n = len(arr)
        for i in range(0, Solution.n):
            tmp = set()
            Len = len(arr[i])
            Solution.sl.append(Len)
            t = True
            for j in range(0, Len):
                if tmp & set(arr[i][j]):
                    t = False
                    break
                tmp.add(arr[i][j])
            if t is False:
                Solution.ok.append(False)
            else:
                Solution.ok.append(True)
            Solution.st.append(tmp)
        print(Solution.ok)
        return Solution.dfs(self, -1, arr, set())


# def main():
#     sol = Solution()
#     print(sol.maxLength(["un","iq","ue"]))


# if __name__ == '__main__':
#     main()
# @lc code=end

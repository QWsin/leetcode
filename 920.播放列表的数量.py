#
# @lc app=leetcode.cn id=920 lang=python3
#
# [920] 播放列表的数量
#
# https://leetcode-cn.com/problems/number-of-music-playlists/description/
#
# algorithms
# Hard (42.76%)
# Likes:    28
# Dislikes: 0
# Total Accepted:    588
# Total Submissions: 1.4K
# Testcase Example:  '3\n3\n1'
#
# 你的音乐播放器里有 N 首不同的歌，在旅途中，你的旅伴想要听 L 首歌（不一定不同，即，允许歌曲重复）。请你为她按如下规则创建一个播放列表：
#
#
# 每首歌至少播放一次。
# 一首歌只有在其他 K 首歌播放完之后才能再次播放。
#
#
# 返回可以满足要求的播放列表的数量。由于答案可能非常大，请返回它模 10^9 + 7 的结果。
#
#
#
# 示例 1：
#
# 输入：N = 3, L = 3, K = 1
# 输出：6
# 解释：有 6 种可能的播放列表。[1, 2, 3]，[1, 3, 2]，[2, 1, 3]，[2, 3, 1]，[3, 1, 2]，[3, 2,
# 1].
#
#
# 示例 2：
#
# 输入：N = 2, L = 3, K = 0
# 输出：6
# 解释：有 6 种可能的播放列表。[1, 1, 2]，[1, 2, 1]，[2, 1, 1]，[2, 2, 1]，[2, 1, 2]，[1, 2, 2]
#
#
# 示例 3：
#
# 输入：N = 2, L = 3, K = 1
# 输出：2
# 解释：有 2 种可能的播放列表。[1, 2, 1]，[2, 1, 2]
#
#
#
#
# 提示：
#
#
# 0 <= K < N <= L <= 100
#
#
#

# @lc code=start

MOD = 10**9 + 7
C = [[] for i in range(110)]
for i in range(110):
    for j in range(i+1):
        if j == i or j == 0:
            C[i].append(1)
        else:
            C[i].append((C[i-1][j] + C[i-1][j-1]) % MOD)


def c(n: int, m: int) -> int:
    if n < 0 or m < 0 or n < m:
        return 0
    return C[n][m]


class Solution:
    def check(self, N: int) -> int:
        return (N % MOD + MOD) % MOD

    def S(self, N: int, L: int, K: int) -> int:
        if K + 1 > N:
            return 0
        res = 1
        for i in range(0, L):
            res = res * max(N-i, N-K) % MOD
        return int(res)

    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        dp = [[] for i in range(N+1)]
        for i in range(K+1, N+1):
            dp[i] = Solution.S(self, i, L, K)
            for j in range(K+1, i):
                dp[i] -= c(i, j) * dp[j] % MOD
            dp[i] = Solution.check(self, dp[i])
        return int(dp[N])
# @lc code=end

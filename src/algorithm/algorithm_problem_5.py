"""
# 5. 最长回文子串

给你一个字符串 s，找到 s 中最长的 回文 子串。

示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"

提示：

1 <= s.length <= 1000
s 仅由数字和英文字母组成
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        ret = s[0]
        if len(s) == 1:
            return s
        # len 大于 1
        for i in range(len(s)):
            # 奇数回文：以 i 为中心
            odd = self.expand(s, i, i)
            if len(odd) > len(ret):
                ret = odd

            # 偶数回文：以 i 和 i+1 为中心
            even = self.expand(s, i, i + 1)
            if len(even) > len(ret):
                ret = even

        # 保底
        return ret

    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]

if __name__ == '__main__':
    sol = Solution()
    a = sol.longestPalindrome("babad")
    print(a)

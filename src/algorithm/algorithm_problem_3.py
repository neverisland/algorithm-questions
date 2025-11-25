"""

定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。

示例 1:

输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。注意 "bca" 和 "cab" 也是正确答案。

示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。


提示：

0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成

"""
class Solution:
    # 这个是暴力求解
    def lengthOfLongestSubstring(self, s: str) -> int:
        longLength = 0
        for i, e in enumerate(s):
            map = {e : 1}
            for char in s[i + 1:]:
                if char in map:
                    break
                map[char] = 1
            print(map)
            longLength = max(longLength, len(map))
        return longLength

    # 滑动窗口
    def lengthOfLongestSubstring1(self, s: str) -> int:
        ans = 0
        curstr = ""
        for i in s:
            if i not in curstr:
                # print(i, curstr)
                curstr = curstr + i
                n = len(curstr)
                if n > ans:
                    ans = n
            else:
                while curstr and curstr[0] != i:
                    curstr = curstr[1:]
                curstr = curstr[1:] + i
        return ans

if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("pwwkew"))


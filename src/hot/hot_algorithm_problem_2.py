"""
49. 字母异位词分组

给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

示例 1:

输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

输出: [["bat"],["nat","tan"],["ate","eat","tea"]]

解释：

在 strs 中没有字符串可以通过重新排列来形成 "bat"。
字符串 "nat" 和 "tan" 是字母异位词，因为它们可以重新排列以形成彼此。
字符串 "ate" ，"eat" 和 "tea" 是字母异位词，因为它们可以重新排列以形成彼此。
示例 2:

输入: strs = [""]

输出: [[""]]

示例 3:

输入: strs = ["a"]

输出: [["a"]]



提示：

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] 仅包含小写字母
"""
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # 排序 + 哈希表（最直观、最常用 ⭐⭐⭐⭐⭐） 时间复杂度：$O(N \cdot K \log K)$
        # 使用 defaultdict，当键不存在时默认返回一个空列表
        map_groups = defaultdict(list)

        for s in strs:
            # 1. 字符串排序：如 "eat" -> ['a', 'e', 't'] -> 拼回字符串 "aet"
            sorted_str = "".join(sorted(s))
            # 2. 放入对应的分组中
            map_groups[sorted_str].append(s)

        # 3. 返回哈希表中的所有分组
        return list(map_groups.values())

        # 计数 + 哈希表（更高效，不需要排序 ⭐⭐⭐⭐）
        map_groups = defaultdict(list)

        for s in strs:
            # 统计 26 个字母出现的次数
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1

            # 将列表转换为 tuple 作为字典的 key（因为 list 不能作为 key）
            key = tuple(count)
            map_groups[key].append(s)

        return list(map_groups.values())

        # 质数相乘哈希（数学巧解，了解即可 ⭐⭐⭐）

        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        map_groups = defaultdict(list)

        for s in strs:
            product = 1
            for char in s:
                product *= primes[ord(char) - ord('a')]
            map_groups[product].append(s)

        return list(map_groups.values())


if __name__ == '__main__':
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
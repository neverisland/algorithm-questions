"""
给你两个非空的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。


示例
1：
输入：l1 = [2, 4, 3], l2 = [5, 6, 4]
输出：[7, 0, 8]
解释：342 + 465 = 807.
示例
2：
输入：l1 = [0], l2 = [0]
输出：[0]
示例
3：
输入：l1 = [9, 9, 9, 9, 9, 9, 9], l2 = [9, 9, 9, 9]
输出：[8, 9, 9, 9, 0, 0, 0, 1]

提示：

每个链表中的节点数在范围[1, 100]
内
0 <= Node.val <= 9
题目数据保证列表表示的数字不含前导零
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    思路：
    1. 获取两个链表的值
    2. 获取两个链表的位数
    3. 计算两个链表的和
    4. 返回组装数据
    """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        value1 = 0
        count1 = 0
        value2 = 0
        count2 = 0
        while l1 is not None:
            value1 += l1.val * (10 ** count1)
            count1 += 1
            l1 = l1.next
        while l2 is not None:
            value2 += l2.val * (10 ** count2)
            count2 += 1
            l2 = l2.next
        sum = value1 + value2

        # 返回组装数据
        node = ListNode(sum % 10)
        sum = sum // 10
        tail = node
        while sum > 0:
            nextNode = ListNode(sum % 10)
            sum = sum // 10
            tail.next = nextNode
            tail = nextNode
        return node

if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    r = s.addTwoNumbers(l1, l2)
    print(r)
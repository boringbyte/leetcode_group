'''
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:
#         string = []
#         while head:
#             string.append(head.val)
#             head = head.next
#         return string == string[::-1]


class Solution:
     def isPalindrome(self, head: ListNode) -> bool:
            if head is None:
                return True
            
            slow = fast = head
            
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                
            prev = None
            while slow:
                current = slow
                slow = slow.next
                current.next = prev
                prev = current
                
            while current and head:
                if current.val != head.val:
                    return False
                head = head.next
                current = current.next
                
            return True
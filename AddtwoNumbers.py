# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1,s2 = "", "" 
        while l1 is not None:
            s1 += str(l1.val)
            l1 = l1.next
        while l2 is not None:
            s2 += str(l2.val)
            l2 = l2.next
        s = str(int(s1[::-1]) + int(s2[::-1]))
        final = []
        for i in xrange(len(s) - 1, -1, -1):
            final.append(int(s[i]))
            
        #final = list(s[::-1])
        return final

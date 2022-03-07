class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = 0
        for x in range(len(l1)):
            result += (l1[x] + l2[x]) * 10**(x)
        result = str(result)[::-1]
        result = list(map(int, result))
        return result

solution = Solution()
L
solution.addTwoNumbers([2,4,3], [5,6,4])
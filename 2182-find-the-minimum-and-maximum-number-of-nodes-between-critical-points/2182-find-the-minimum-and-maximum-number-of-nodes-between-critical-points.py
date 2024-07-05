# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        left = head
        mid = head.next
        if not mid.next:
            return [-1,-1]
        right = mid.next
        critical = []
        i = 2
        while right:
            if (mid.val > left.val and mid.val > right.val) or (mid.val < left.val and mid.val < right.val):
                critical.append(i)
            i += 1
            left = mid
            mid = right
            right = right.next

        if len(critical) <= 1:
            return [-1,-1]
        
        min_dist = float('inf')
        for i in range(1,len(critical)):
            min_dist = min(min_dist, critical[i] - critical[i-1])
        max_dist = critical[-1] - critical[0]

        return [min_dist, max_dist]
        
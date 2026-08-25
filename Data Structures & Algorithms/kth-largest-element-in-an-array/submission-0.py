class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []
        res = float("-inf")

        for n in nums:
            heapq.heappush(max_heap, (-1 * n))
        
        for i in range(k):
            res = -1 * heapq.heappop(max_heap)

        return res

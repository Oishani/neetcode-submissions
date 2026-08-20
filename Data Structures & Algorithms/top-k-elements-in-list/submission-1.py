class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_count = Counter(nums)
        max_heap = []
        result = []

        for num, count in num_to_count.items():
            heapq.heappush(max_heap, (-count, num))

        for i in range(k):
            count, num = heapq.heappop(max_heap)
            result.append(num)
        
        return result
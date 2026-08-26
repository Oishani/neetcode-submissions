class MedianFinder:

    def __init__(self):
        self.left_max_heap = []
        self.right_min_heap = []
        heapq.heapify(self.left_max_heap)
        heapq.heapify(self.right_min_heap)
        

    def addNum(self, num: int) -> None:
        max_num = -1 * self.left_max_heap[0] if self.left_max_heap else float("-inf")
        min_num = self.right_min_heap[0] if self.right_min_heap else float("inf")

        if num > min_num:
            heapq.heappush(self.right_min_heap, num)
        else:
            heapq.heappush(self.left_max_heap, -1 * num)
        
        if len(self.left_max_heap) - len(self.right_min_heap) > 1:
            n = -1 * heapq.heappop(self.left_max_heap)
            heapq.heappush(self.right_min_heap, n)
        elif len(self.right_min_heap) - len(self.left_max_heap) > 1:
            n = heapq.heappop(self.right_min_heap)
            heapq.heappush(self.left_max_heap, -1 * n)

    def findMedian(self) -> float:

        if len(self.left_max_heap) == len(self.right_min_heap):
            max_val = -1 * self.left_max_heap[0]
            min_val = self.right_min_heap[0]
            return (max_val + min_val) / 2
        elif len(self.left_max_heap) > len(self.right_min_heap):
            return -1 * self.left_max_heap[0]
        else:
            return self.right_min_heap[0]
        
        
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        import collections
        counter = collections.Counter(words)
        heap = []
        for word, freq in counter.items():
            heap.append((-freq, word))
        heapq.heapify(heap)
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result
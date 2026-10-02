class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fre = {}
        res = []
        for i in nums:
            fre[i] = fre.get(i,0)+1
        sorted_freq = sorted(fre,key=fre.get,reverse = True)
        return sorted_freq[:k]

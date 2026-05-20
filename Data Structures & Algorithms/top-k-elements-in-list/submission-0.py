class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count_map = {}

        for num in nums:              # key is the number, value is the frequency
            if num in count_map:
                count_map[num] += 1 
            else:
                count_map[num] = 1
        
        buckets = [[] for i in range(len(nums) + 1)]

        for num, freq in count_map.items():
            buckets[freq].append(num)

        res = []

        for n in range(len(buckets) - 1, 0, -1):
            for num in buckets[n]:
                res.append(num)

                if len(res) == k:
                    return res




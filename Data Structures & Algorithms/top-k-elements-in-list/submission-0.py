class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # k is number of integers you return 

        seen = {}
        output = []
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1

        for i in range(k):
            mostFrequent = max(seen, key=seen.get)
            output.append(mostFrequent)
            seen.pop(mostFrequent)
        return output




        


        
        
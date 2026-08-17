class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # k is number of integers you return 
        #dictonary stores number and frequency number apears in array 
        frequencyDictonary = {}
        for num in nums:
            if num in frequencyDictonary:
                frequencyDictonary[num] += 1
            else:
                frequencyDictonary[num] = 1
        # creates a list of tempoarary filled buckets that will be filled in based on frequency of numbers 
        buckets = []
        for i in range(len(nums) + 1):
            buckets.append([])
        #puts number at correct bucket depending on frequency 
        for num in frequencyDictonary:
            frequency = frequencyDictonary[num]
            buckets[frequency].append(num)
        #create output list
        output = []
        for bucket in reversed(buckets):
            for values in bucket:
                output.append(values)
                if len(output) == k:
                    return output
        




        


        
        
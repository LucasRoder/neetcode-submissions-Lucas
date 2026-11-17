class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        numCounter = {}
        for num in nums:
            if num in numCounter:
                numCounter[num] += 1
            else:
                numCounter[num] = 1

        largeNum = []
        for i in range(2):
            while True:
                large = max(numCounter) 
                if numCounter[large] != 0:
                    numCounter[large] -= 1
                    largeNum.append(large)
                    break
                else:
                    del numCounter[large]
                    

        smallNum = []
        for i in range(2):        
            while True:
                small = min(numCounter) 
                if numCounter[small] != 0:
                    numCounter[small] -= 1
                    smallNum.append(small)
                    break
                else:
                    del numCounter[small]

        large = largeNum[0] * largeNum[1]
        small = smallNum[0] * smallNum[1]

        return large - small
            

        
            




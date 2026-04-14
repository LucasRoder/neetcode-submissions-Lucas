class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0;
        while i < k:
            back = nums.pop(len(nums)-1)
            nums.insert(0, back)
            i = i + 1
            
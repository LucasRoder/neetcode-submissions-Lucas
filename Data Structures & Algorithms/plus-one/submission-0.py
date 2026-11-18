class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""

        for digit in digits:
            num += str(digit)

        num = int(num)
        num += 1
        num = str(num)

        output = []
        for n in num:
            output.append(int(n))

        return output





        
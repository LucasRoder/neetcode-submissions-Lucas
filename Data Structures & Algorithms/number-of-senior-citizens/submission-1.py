class Solution:
    def countSeniors(self, details: List[str]) -> int:
        output = 0
        for digits in details:
            age = digits[11] + digits[12]
            age = int(age)

            if age > 60:
                output += 1

        return output

        
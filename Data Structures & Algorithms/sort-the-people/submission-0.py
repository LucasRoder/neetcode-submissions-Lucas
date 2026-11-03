class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        output = []
        people = {}
        for i in range(len(names)):
            people[heights[i]] = names[i]

        sortedDict = sorted(people.items(), reverse = True)

        for val in sortedDict:
            output.append(val[1])

        return output
        
        
            
            
        
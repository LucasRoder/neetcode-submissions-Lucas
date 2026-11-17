class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        destinationMap = {}
        for path in paths:
            destinationMap[path[0]] = path[1]

        for path in paths:
            for location in path:
                if location not in destinationMap:
                    return location



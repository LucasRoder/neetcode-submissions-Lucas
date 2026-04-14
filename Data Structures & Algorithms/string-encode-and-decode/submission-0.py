class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for string in strs:
            for char in string:
                output += str(ord(char))
                output += ","
            output += "|"
        
        return output
            
    def decode(self, s: str) -> List[str]:
        words = s.split("|")
        output = []
        for word in range(len(words) -1 ):

            chars = words[word].split(",")

            decodeList = []
            for char in chars:
                if char == "":
                    continue 
                decodeList.append(chr(int(char)))
            output.append("".join(decodeList))
            

        return output

        


class Solution:

    def encode(self, strs: List[str]) -> str:
        for i in range(len(strs)):
            strs[i] = str(len(strs[i])) + "#" + str(strs[i])
        return "".join(strs) + "200"
        

    def decode(self, s: str) -> List[str]:
        position = 0
        res = []

        while s[position:] != "200":

            char_length_string = s[position]
            char_length_helper = 1
            while s[position + char_length_helper] != "#":
                char_length_string += s[position+char_length_helper]
                char_length_helper += 1
            char_length = int(char_length_string)

            length_of_char_length = len(str(char_length))
            
            res.append(s[position+length_of_char_length+1:position+length_of_char_length+1+char_length])
            position = position + length_of_char_length+1 + char_length

        return res


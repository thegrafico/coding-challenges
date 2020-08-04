"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows 
like this: (you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R

================================================
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"

P     I    N
A   L S  I G
Y A   H R
P     I

=================================================
"""

class Solution:
    def convert(self, s: str, numRows:int) ->str:
        
        
        if numRows == 1 or len(s) == 0 or len(s) <= numRows:
            return s
        
        # print(s)
        matrix = []
        sub_matrix = {}
        number = 0
        reverse = False
        firts_time = True
        for i, char in enumerate(s):
            
            #get the number i
            number = self.going_down(number) if reverse else self.going_up(number)
            
            sub_matrix[number] = char
            
            if number == (numRows):
                matrix.append( { k: sub_matrix[k] for k in sorted(sub_matrix)} )
                reverse = True
                sub_matrix = {}
            elif number == 1:
                if firts_time:
                    firts_time = False
                else:
                    matrix.append( { k: sub_matrix[k] for k in sorted(sub_matrix, reverse=True)} )
                    sub_matrix = {}
                reverse = False 

        print("{} == {}, number: {}".format(i, len(s) -1,numRows))
        
        if len(sub_matrix) > 0:
            matrix.append(sub_matrix)
            sub_matrix = {}            
        out = ""
        for i in range(1, numRows+1):
            for sub in matrix:
                if i in sub.keys():
                    out += sub[i]
        # print(out)
        return out     
            
    def going_down(self, number:int) -> int:
        return number - 1

    def going_up(self, number:int) -> int:
        return number + 1 
#-- Test
if __name__ == "__main__":
    solution = Solution()
    test = "ABC"
    print(test)
    numRows = 2
    print(solution.convert(test, numRows))
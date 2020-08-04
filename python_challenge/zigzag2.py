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
    def convert(self, s: str, numRowns:int) ->str:
      pass
#-- Test
if __name__ == "__main__":
    solution = Solution()
    test = "PAYPALISHIRING"
    numRows = 5
    solution.convert(test, numRows)
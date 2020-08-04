"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
"""

def longestPalindrome(s: str) -> str:
        tam = len(s)
        all_palindromes = {}
        if tam == 0:
            return ""
        
        if len(list(set(s))) == tam:
            return s[0]
        
        index_pos = {}
        for char in s:
            if char not in index_pos.keys():
                index_pos[char] = [index for index in range(tam) if s[index] == char]
        # print(index_pos)
        for values in index_pos.values():
            if len(values) > 1:
                # print(values)
                for i in range(len(values)):
                    for j in range(len(values)-1, -1, -1):
                        # print("Start: {}, End: {}".format(j, len(values)))
                        if i != j:
                            string = s[ values[i] : values[j] + 1]

                            if string != "" and string == string[::-1]:
                                # print(string, "==>", string[::-1])
                                if string not in all_palindromes.keys():
                                    all_palindromes[string] = len(string)
        print(all_palindromes)
        return max(all_palindromes, key=all_palindromes.get) if len(all_palindromes) > 0 else s[0]
#-- 
# test = "abacab"
test = "abcd"
test = "abcda"
print(longestPalindrome(test))
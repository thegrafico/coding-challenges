"""
Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.

Input: "abcabcbb"
Input = "dvdf"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
"""

class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:

		#Return if there is not elements to go over
		if len(s) < 2: 
			return len(s)
	
		self.elements = []
		self.max = 0
  
		for i in range(len(s)):
			self.elements = []
			for j in range(i,len(s)):
				if self.verify(s[j]):
					if self.max < len(self.elements):
						self.max = len(self.elements)
				else:
					break
		return self.max
    #-- Another func	
	def verify (self, char:str) ->  bool:
		if char not in self.elements:
			self.elements.append(char)
			return True
		return False


longest = Solution()

s = "pwwkew"
print("EVALUATING =>", s)
print(longest.lengthOfLongestSubstring(s))
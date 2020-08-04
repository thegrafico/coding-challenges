"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
	'.' Matches any single character.
	'*' Matches zero or more of the preceding element.

	The matching should cover the entire input string (not partial).

	Note:
	s could be empty and contains only lowercase letters a-z.
	p could be empty and contains only lowercase letters a-z, and characters like . or *.

	Ex:
	Input:
	s = "aa"
	p = "a"
	Output: false
	Explanation: "a" does not match the entire string "aa".

	Input:
	s = "aa"
	p = "a*"
	Output: true
	Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

	Input:
	s = "ab"
	p = ".*"
	Output: true
	Explanation: ".*" means "zero or more (*) of any character (.)".

	Input:
	s = "aab"
	p = "c*a*b"
	Output: true
	Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".

	Input:
	s = "mississippi"
	p = "mis*is*p*."
	Output: false
"""


def match_regex(s: str, p: str) -> bool:
	"""
	:param s: string to match
	:param p: pattern for string
	:return: True if string match with pattern
	"""

	if '.' not in p and '*' not in p:
		if s != p:
			return False
		else:
			return True
	else:
		index_s, index_p = 0, 0
		last_char = None
		new_string = ''
		try:
			while True:

				if (p[index_p] == s[index_s] or p[index_p] == '.') and (p[index_p + 1] != '*'):
					last_char = s[index_s]
					new_string += last_char

					index_p += 1
					index_s += 1

					if index_p == len(p):
						return new_string == s
	
					print('HERE 1')
				elif p[index_p] == '*':
					print('HERE 2')
					if last_char == s[index_s]:
						index_s += 1
						new_string += last_char
					else:
						index_p += 1
						last_char = s[index_s]
				else:
					break
				print(new_string)
		except Exception as e:
			print(e)
	return new_string == s

if __name__ == '__main__':
	string = 'aaab'
	pattern = 'a*be*'

	print(match_regex(s=string, p=pattern))

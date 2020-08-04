"""
Find the max occurrence
"""

def max_move(s,t):
    done = False
    count = 0
    while not done:
        if t in s:        
            # print(s)
            s = s.replace(t, "",1)
            # print(s)
            count+=1
            # print(count)
        else:
            done = True
    return count

def find_index_ocurrence(s, t):
    occurence_index = []
    for i in range(len(s)):
        for j in range(len(s)):

            #Count occurence
            if s[i:j] == t:
                occurence_index.append([i, j])
                # print(s[i:j], i, j)
    return occurence_index if len(occurence_index) > 0 else -1
        


# s = "abcaabcbababcc"
# t = "abc"

s= "abababaabaabababaaba"
t = "ababa"
print("Looking for {} in ==> {}".format(t, s))

# print(max_move(s,t))
print(find_index_ocurrence(s,t))

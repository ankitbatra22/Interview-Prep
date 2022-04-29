# 242. Valid Anagram most efficient solution

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            s_dict = {}
            t_dict = {}
            for i in s:
                if i in s_dict:
                    s_dict[i] += 1
                else:
                    s_dict[i] = 1
            for i in t:
                if i in t_dict:
                    t_dict[i] += 1
                else:
                    t_dict[i] = 1
            for i in s_dict:
                if i not in t_dict:
                    return False
                elif s_dict[i] != t_dict[i]:
                    return False
            return True

# uses a dictionary to store the frequency of each character in the string.
# time and space: O(n)

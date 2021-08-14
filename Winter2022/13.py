values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }


class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        p = 0
        
        while p < len(s):
            
            #subtractive case
            if p + 1 < len(s) and values[s[p]] < values[s[p + 1]]:
                total += values[s[p + 1]] - values[s[p]]
                p += 2
                
            #not the subtractive case.
            else:
                total += values[s[p]]
                p += 1
        return total

# O(1) space
# O(1) time

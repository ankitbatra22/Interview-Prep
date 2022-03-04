class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # want seq_idx == len(sequence)
        arr_idx = 0
        seq_idx = 0
        while arr_idx < len(t) and seq_idx < len(s):
            if t[arr_idx] == s[seq_idx]:
                seq_idx+=1
            arr_idx+=1
        
        return seq_idx == len(s)
        
# Runs in O(n) time and O(1) space.
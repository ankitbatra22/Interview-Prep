class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        seqIdx = 0
        if s == t:
            return True
        for value in t:
            if len(s) == seqIdx:
                break
            if value == s[seqIdx]:
                seqIdx += 1
        return seqIdx == len(s)

# Runs in O(n) time and O(1) space.
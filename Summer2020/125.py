class Solution:
    def isValid(self, s: str) -> bool:
      brackets = {')':'(', '}':'{', ']':'['}

      stack  = []
      for char in s:
        if char in brackets:
          if stack:
            top = stack.pop()
          else:
            top = ""
        
        if brackets[char] != top:
          return False
        else:
          stack.append(char)


      return not stack


# -- Alternate --
      def isValid(self, s: str) -> bool:
        stack = []
        key = {"]":"[", "}":"{", ")":"("}
        
        for char in s:
            if char in key.values():
                stack.append(char)
            else:
                if len(stack) > 0 and stack[-1] == key[char]:
                    stack.pop()
                else:
                    return False
        
        if (len(stack) == 0):
            return True





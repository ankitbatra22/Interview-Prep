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

          
      
"""dict = {'(':')', '{':'}', '[':']'}
print(dict["{"])"""

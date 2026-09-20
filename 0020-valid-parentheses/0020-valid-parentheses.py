class Solution(object):

  def isValid(self, s):
    # Quick optimization: odd length strings can never be balanced
    if len(s) % 2 != 0:
      return False

    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
      if char in mapping:
        # Pop the top element if stack is not empty, else assign a dummy value
        top_element = stack.pop() if stack else "#"

        # Check if the popped bracket matches the expected opening bracket
        if mapping[char] != top_element:
          return False
      else:
        # It's an opening bracket, push onto stack
        stack.append(char)

    # Valid if no unmatched opening brackets remain
    return not stack
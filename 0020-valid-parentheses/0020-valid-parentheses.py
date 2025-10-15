class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mapping_parentheses = {"(": ")", "[": "]", "{": "}"}

        for char in s:
            if char in mapping_parentheses:
                stack.append(mapping_parentheses[char])
            elif not stack or stack.pop() != char:
                return False
        
        return False if stack else True

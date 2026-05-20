class Solution:
    def isValid(self, s: str) -> bool:
        # stack that gets openbrackets and closing them by left brackets by poping them.
        stack = []
        mapping = {
            ')':'(',
            ']':'[',
            '}':'{',
        }

        for ch in s:
            if ch in mapping.values():
                stack.append(ch)
            else:
                if not stack or stack.pop() != mapping[ch]:
                    return False
        return len(stack) == 0
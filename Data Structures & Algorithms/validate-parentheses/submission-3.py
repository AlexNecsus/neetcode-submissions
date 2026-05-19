class Solution:
    def isValid(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        stack = []
        mapping = {
            ')':'(',
            '}':'{',
            ']':'[',
        }
        for b in s:
            if b in mapping.values():
                stack.append(b)
            else:
                if not stack or stack.pop() != mapping[b]:
                    return False

        return len(stack) == 0
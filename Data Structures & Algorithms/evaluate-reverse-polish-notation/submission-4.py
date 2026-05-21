class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # I can create function for each notation, or use needed operators by changing indication value 
        # but i think it'll be inefficient 
        res = []

        for i in tokens:
            if i == "+":
                res.append(res.pop() + res.pop())
            elif i == "-":
                a, b = res.pop(), res.pop()
                res.append(b - a)
            elif i == "*":
                res.append(res.pop() * res.pop())
            elif i == "/":
                a, b = res.pop(), res.pop()
                res.append(int(b / a))
            else:
                res.append(int(i))
        return res[0] 
class Solution:
    def isValid(self, s: str) -> bool:
        paranthesis = { "(" : ")", "[" : "]", "{" : "}" }
        mapp = []
        if len(s) % 2 == 0:
            for v in s:
                if v in paranthesis.keys():
                    mapp.append(v)
                else:
                    key = ''
                    for r, y in paranthesis.items():
                        if v == y:
                            key = r
                            break
                    if key != '':
                        if mapp == []:
                            return False
                        if mapp[-1] == 0:
                            return False
                        if key == mapp[-1]:
                            mapp.pop()
                        else:
                            return False
                    else:
                        return False
        else:
            return False
        return len(mapp) == 0
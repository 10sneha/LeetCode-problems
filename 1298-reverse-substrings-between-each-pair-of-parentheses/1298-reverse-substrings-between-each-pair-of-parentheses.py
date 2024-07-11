class Solution:
    def reverseParentheses(self, s: str) -> str:
        stk = []
        for i in s:
            if i == ")":
                j = stk.pop()
                st = ""
                while j != "(":
                    st += j
                    j = stk.pop()
                for j in st:
                    stk.append(j)
            else:
                stk.append(i)
            print(stk)
        return "".join(stk)
        
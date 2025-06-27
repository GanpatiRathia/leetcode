class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for it in s:
            if it == '(' or it == '{' or it == '[':
                st.append(it)
            else:
                if len(st) == 0:
                    return False
                ch = st[-1]
                st.pop()
                if (it == ')' and ch == '(') or (it == ']' and ch == '[') or (it == '}' and ch == '{'):
                    continue
                else:
                    return False
        return len(st) == 0
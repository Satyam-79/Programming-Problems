class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        st=[]
        res=""
        for c in s:
            if len(st)==0:
                st.append(c)
            elif len(st)==1 and c==')':
                st.pop()
            else:
                if c == '(':
                    st.append(c)
                    res+=c
                else:
                    st.pop()
                    res+=c
        return res
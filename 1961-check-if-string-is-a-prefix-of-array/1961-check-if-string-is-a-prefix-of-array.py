class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        res=""
        for w in words:
            res+=w
            if res==s:
                return True
        else:
            False
            
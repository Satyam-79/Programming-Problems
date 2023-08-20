class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count=Counter(stones)
        res=0
        for j in jewels:
            res+=count.get(j,0)
        return res
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr=[]
        arr.append(first)
        for en in encoded:
            arr.append(arr[-1]^en)
        return arr
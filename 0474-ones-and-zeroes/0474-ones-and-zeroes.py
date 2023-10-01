class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        binary_list=[]
        for s in strs:
            count=Counter(s)
            binary_list.append([count['0'],count['1']])
            
        @cache
        def rec(idx,z,o):
            if z==o==0 or idx >=len(binary_list):
                return 0
            exc=rec(idx+1,z,o)
            zeros, ones=binary_list[idx]
            if zeros<=z and ones<=o:
                inc=1 + rec(idx+1,z-zeros,o-ones)
                return max(inc,exc)
            return exc
        
        return rec(0,m,n)
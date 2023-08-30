class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n=len(customers)
        penalty=float('inf')
        day=0
        y_count=0
        n_count=0
        for c in customers:
            if c=='Y':
                y_count+=1
        if y_count==n:
            return n
        elif y_count==0:
            return 0
        penalty=y_count
        
        
        for i in range(n):
            c=customers[i]
            if c=='Y':
                y_count-=1
            else:
                n_count+=1
            
            if penalty>y_count+n_count:
                penalty=y_count+n_count
                day=i+1
        return day
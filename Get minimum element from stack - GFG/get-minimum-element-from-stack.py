#User function Template for python3

class stack:
    def __init__(self):
        self.A = []
        self.M = []

    def push(self,x):
        self.A.append(x)
        self.M.append(x if not self.M else min(x, self.M[-1]))

    def pop(self):
        if self.A:
            self.M.pop()
            return self.A.pop()
        else:
            return -1
        

    def getMin(self):
        if self.M:
            return self.M[-1]
        else:
            return -1


#{ 
 # Driver Code Starts
#contributed by RavinderSinghPB
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        q = int(input())

        arr = [int(x) for x in input().split()]

        stk=stack()  

        qi = 0
        qn=1
        while qn <= q:
            qt = arr[qi]

            if qt == 1:
                stk.push(arr[qi+1])
                qi+=2
            elif qt==2:
                print(stk.pop(),end=' ')
                qi+=1
            else:
                print(stk.getMin(),end=' ')
                qi+=1
            qn+=1
        print()

# } Driver Code Ends
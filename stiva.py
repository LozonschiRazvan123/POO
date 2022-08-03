class MaxStack():
    def __init__(self):
        self.main=[]
        self.max=[]
        self.maxi=0
        self.pos=0

    def push(self,n):
        if len(self.max)==0:
            self.max.append(n)
        elif n<=self.max[-1]:
            self.max.append(self.max[-1])
        else:
            self.max.append(n)
        self.main.append(n)

    def pop(self):
        self.max.pop()
        return self.main.pop()

    def get_min(self):
        return self.max[-1]


    def solve(self):
        for i in self.max:
            self.max[i] = self.max[i+1]
            if self.max[i]>self.maxi:
                self.maxi=self.max[i]
                self.pos=i



stack=MaxStack()
stack.push(3)
stack.push(4)
stack.push(3)
stack.push(5)
stack.push(1)
print(stack.max)

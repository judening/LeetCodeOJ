class MinStack:
    # The idea is to set up a minimum array to monitor the minimum num

    def __init__(self):
        self.arry = []
        self.minimum = []

    def push(self,x):
        if not self.minimum:
            self.minimum.append(x)
        else:
            lastMin = self.minimum[-1]
            #we only save it when x<=lastMin, that case it will save memory
            if x <= lastMin:
                self.minimum.append(x)
        self.arry.append(x)

    def pop(self):
        if not self.arry:
            return
        else:
            if self.arry.pop() == self.minimum[-1]:
                self.minimum.pop()

    def top(self):
        if not self.arry:
            return None
        else:
            return self.arry[-1]

    def getMin(self):
        if not self.arry:
            return None
        else:
            return self.minimum[-1]

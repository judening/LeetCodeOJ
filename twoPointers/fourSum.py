class Solution:
    def fourSum(self,num,target):
        numLen, rez, d = len(num), set(), {}
        if numLen<4: return []
        num.sort()
        for p in xrange(numLen):
            for q in xrange(p+1,numLen):
                if num[p]+num[q] not in d:
                    d[num[p]+num[q]] = [(p,q)]
                else:
                    d[num[p]+num[q]].append((p,q))
        for i in xrange(numLen):
            for j in xrange(i+1,numLen-2):
                T = target - num[i]-num[j]
                if T in d:
                    for k in d[t]:
                        if k[0]>j:
                            rez.add((num[i],num[j],num[k[0]],num[k[1]])
        return [list(i) for i in rez]

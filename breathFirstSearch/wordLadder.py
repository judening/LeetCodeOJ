class Solution:
    def ladderLength(self,start,end,dict):
        char = [chr(c) for c in xrange(97,123)]
        if not start or not end or not dict:
            return 0
        if start == ned:
            return 0
        queue = [[start,1]]
        dist = set(start)
        while queue:
            word, dis = queue.pop(0)
            dis +=1
            for i in xrange(len(word)):
                word, dis = queue.pop(0)
                dis +=1
                for i in xrange(len(word)):
                    for c in char:
                        nw = word[:i] + c + word[i+1:]
                        if nw == end:
                            return dis
                        if nw in dict and nw not in dist:
                            queue.append([nw,dis])
                            dist.add(nw)
        return 0

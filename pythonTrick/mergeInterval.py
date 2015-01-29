class Solution:
    def merge(self,intervals):
        if intervals:
            intervals = sorted(intervals, key = lambda interval:interval.start)
            toRet = []
            pre = None
            for interval in intervals:
                if pre:
                    if interval.start > pre.end:
                        toRet.append(pre)
                        pre = interval
                    else:
                        pre.end = max(interval.end,pre.end)
            toRet.append(pre)
            return toRet
        else:
            return []

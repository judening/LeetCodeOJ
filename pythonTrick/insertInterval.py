class Solution:
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        if len(intervals) == 0:
            return intervals
        # I gotta say this is too beautiful
        # Never ever thought of the lambda function can be used here
        intervals = sorted(intervals, key = lambda x: x.start)
        ret = []
        ret.append(intervals[0])
        for interval in intervals:
            if interval.start > ret[-1].end:
                ret.append(interval)
            else:
                ret[-1].end = max(ret[-1].end,interval.end)
        return ret


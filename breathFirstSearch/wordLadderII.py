import collections
import string

# This is not only a "completed" BFS, but also a backward tracking problems

class Solution:
    # @param dict, a "set" of string
    # @return a list of lists of string
    def findLadders(self,start,end,dict):
        dict.add(end)
        level = {start}
        # Parent is a dictionary that its value is all set
        # By using defaultdict, it sets up all the defalut value
        # The keys of parents are strings and the values of them
        # are set
        # To be more specific, the keys are actually the "children", AKA
        # next possible ladder, and the val is the "parent"
        parents = collections.defaultdict(set)
        # Why this for loop will eventually stop?
        # 1. level here is reinitialized every single time after the loop
        # 2. end in parents (which means that we already find all the possible ways)
        while level and end not in parents:
            # Each next_level is a new defaultdict
            next_level = collections.defaultdict(set)
            for node in level:
                # Based on the keys in last level
                # We are connecting the values with keys (lower ladder with
                # upper ladder)
                # from here
                for char in string.ascii_lowercase:
                    for i in xrange(len(start)):
                        n = node[:i]+char+node[i+1:]
                        if n in dict and n not in parents:
                            next_level[n].add(node)
                # to there is exactly the same with word ladder one
            level = next_level
            # The update function of dictionary doesn't necessary
            # wipe out the old data, just like its function name,
            # it is UPDATING the sets
            parents.update(next_level)
        res = [[end]]
        while res and res[0][0] != start:
            # Geez this for loop is really obscure
            # It is literally
            # for r in res:
            #     for p in parents[r[0]]:
            # It's really easy to get confused here
            # 1. r is a list
            # 2. for r in res means for all the possible lists
            #    we keep adding up the children, AKA upper ladder,
            #    uptill we hit the start
            res = [[p] + r for r in res for p in parents[r[0]]
        return res


class Solution:
    # The ultimate question here is how I know that
    # the returned distance is the minimum distance?
    # The trick is BFS with a little bit of tracking
    # We end the search once we find the word amongst
    # the candidates of the same distances
    # Once we hit the end, we stop searching.
    # Unlike DFS, which go as deep as possible for each candidate, BFS
    # here ensure that we return asap
    def ladderLength(self,start,end,dict):
        # Thought process:
        # 1.Create a list to store all the char from a-zA-Z
        char = [chr(c) for c in xrange(97,123)]
        # PS. quick check whether start/end is in dict
        if not start or not end or not dict:
            return 0
        if start == ned:
            return 0
        # Think of queue as a list of storing a list of array
        queue = [[start,1]]
        dist = set(start)
        while queue:
            # 2. Pop all the possible candidates that are in dict
            word, dis = queue.pop(0)
            # ps: This increment can be put in the following for loops
            # putting here might be confusing but actually it make senses
            # we are not recording the "failure" distance in the dictionary
            # anyways
            dis += 1
            for i in xrange(len(word)):
                # This is delicate
                # we substitue the word letter each time to find all the
                # possible candidates
                for c in char:
                    # 3. Subsitute letter one by one and find the best
                    # answer
                    nw = word[:i] + c + word[i+1:]
                    if nw == end:
                        return dis
                    if nw in dict and nw not in dist:
                        queue.append([nw,dis])
                        dist.add(nw)
        return 0

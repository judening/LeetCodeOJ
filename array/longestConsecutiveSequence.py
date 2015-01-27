class Solution:
    def longestConsecutive(self,num):
        cache = {}
        visited = {}
        for i in xrange(len(num)):
            cache[num[i]] = 1
        longest = 1
        for n in num:
            cn = 1
            prev = n-1
            while prev in cache and prev not in visited:
                visited[prev]=1
                prev -=1
                cn +=1
            next  = n+1
            while next in cache and next not in visited:
                visited[next] =1
                next +=1
                cn+=1
            if cn>longest:
                longest = cn
        return longest

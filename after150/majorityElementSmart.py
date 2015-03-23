class Solution:
    # Based on the question, the majority element always appears
    # more than floor(n/2) times. Thus, the number of times it
    # appears must >= the sum of the rest of the elements
    # Thus, you can get the following method
    def majorityElement(self,num):
        counter = 1
        major = num[0]
        for i in xrange(1,len(num)):
            if counter == 0:
                counter +=1
                major = num[i]
            elif major == num[i]:
                counter+=1
            else:
                counter-=1
        return major

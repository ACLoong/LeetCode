class Solution:
    def countAndSay(self, n):
        """
        Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

        Args:
            n(int): the given integer n

        Returns:
             the nth term of the count-and-say sequence(str)
        """
        num = "1"
        for i in range(1, n):
        	num = self.next(num)
        return num

    def next(self, num):
    	res = ""
    	prev = num[0]
    	cnt = 1
    	for i in range(1, len(num)):
    		if num[i] == prev:
    			cnt += 1
    		else:
    			res += str(cnt)
    			res += num[i-1]
    			prev = num[i]
    			cnt = 1
    	res += str(cnt)
    	res += num[-1]
    	return res
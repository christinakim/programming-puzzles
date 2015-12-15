class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in range(2, n):
            if self.is_prime(i):
                res += 1
        return res

    def is_prime(self, k):
        i = 2
        while i * i <= k:
            if k % i == 0:
                return False
            i += 1
        return True


s = Solution()
print(s.countPrimes(500))
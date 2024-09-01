class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        l = len(original)
        if m*n != l:
            return []

        for i in range(0,l,n):
            res.append(original[i:i+n])
        return res

        
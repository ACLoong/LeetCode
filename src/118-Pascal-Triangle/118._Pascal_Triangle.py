class Solution:
    def generate(self, numRows):
        """
        Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

        Args:
            numRows(int): the given non-negative integer

        Returns:
            the first numRows of Pascal's triangle(List[List[int]])
        """
        result = [[1]*(i+1) for i in range(numRows)]
        for i in range(numRows):
            for j in range(1,i):
                result[i][j] = result[i-1][j-1] + result[i-1][j]
        return result

class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        M = len(matrix)
        N = len(matrix[0])
        for offset in range(-M+1,N):
            diag = [row[i + offset] for i, row in enumerate(matrix) if 0 <= i + offset < len(row)]
            if(False == all(x == diag[0] for x in diag)):
                return False
        return True
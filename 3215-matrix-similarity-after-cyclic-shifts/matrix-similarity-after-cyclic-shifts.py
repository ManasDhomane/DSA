class Solution:
    def areSimilar(self, mat, k):
        m = len(mat)
        n = len(mat[0])

        shift = k % n

        for i in range(m):
            for j in range(n):

                if i % 2 == 0:
                    new_pos = (j - shift) % n
                else:
                    new_pos = (j + shift) % n

                if mat[i][j] != mat[i][new_pos]:
                    return False

        return True
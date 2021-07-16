
#旋转四次：四个位置同时循环交换，所以不需要中间变量
#1.matrix_new[col][n−row−1]=matrix[row][col]
#2.matrix[col][n−row−1]=matrix[row][col]
#3.matrix[n−row−1][n−col−1]=matrix[col][n−row−1]
#4.matrix[n−col−1][row]=matrix[n−row−1][n−col−1]

#迭代次数
#偶数：将矩阵分为上下左右四块，只需迭代完其中一块的元素就能实现整个矩阵旋转交换完成
#奇数：中间一个元素位置不变，将其余元素划分为(n-1)/2 * (n+1)/2元素块，也是只需迭代完其中一块的元素就能实现整个矩阵旋转交换完成
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] \
                    = matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]

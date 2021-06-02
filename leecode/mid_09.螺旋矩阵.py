#输入矩阵，按照顺时针方向螺旋向内输出各个元素

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]: return []
        M, N = len(matrix), len(matrix[0])   #获取矩阵的行数和列数
        left, right, up, down = 0, N - 1, 0, M - 1   #定义上下左右边界
        res = []
        x, y = 0, 0          #元素位置坐标
        # 表示移动方向4*2矩阵，第一行表示向右遍历，第二行表示向下遍历，第三行表示向左遍历，第四行表示向上遍历
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cur_d = 0    #表示当前移动方向的下标
        #每次遍历完一行或一列后修改边界
        while len(res) != M * N:
            res.append(matrix[x][y])
            if cur_d == 0 and y == right:
                cur_d += 1
                up += 1
            elif cur_d == 1 and x == down:
                cur_d += 1
                right -= 1
            elif cur_d == 2 and y == left:
                cur_d += 1
                down -= 1
            elif cur_d == 3 and x == up:
                cur_d += 1
                left += 1
            cur_d %= 4
            x += dirs[cur_d][0]
            y += dirs[cur_d][1]
        return res
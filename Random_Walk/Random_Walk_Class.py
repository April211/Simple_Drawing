from random import choice

class RandomWalk:
    """一个生成随机漫步数据的类"""

    def __init__(self, num_points=5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points

        # 记录随机漫步的坐标点，所有随机漫步都开始于：(0, 0)
        self.x_values = [0]
        self.y_values = [0]
    # end

    def fill_walk(self):
        """计算随机漫步包含的所有点"""

        # 不断漫步，直到列表到达指定的长度
        while len(self.x_values) < self.num_points:

            # 决定前进方向以及沿这个方向前进的距离（当该次 step等于 0时，表示该次走步沿该轴不移动）
            x_direction = choice([1, -1])
            x_step = choice([0, 1, 2, 3, 4])
            x_distance = x_direction* x_step

            y_direction = choice([1, -1])
            y_step = choice([0, 1, 2, 3, 4])
            y_distance = y_direction* y_step

            # 拒绝原地踏步（即两个方向上行走的距离都是 0）
            if (x_distance == 0) and (y_distance == 0):
                continue

            # 计算下一个点的 X值和 Y值（在上一个点，即当前列表的最后一个元素的基础上，加上该次的在两个方向上的距离）
            x = self.x_values[-1] + x_distance
            y = self.y_values[-1] + y_distance

            # 将新生成的坐标值分别加入到两个列表中
            self.x_values.append(x)
            self.y_values.append(y)
    # end
# end

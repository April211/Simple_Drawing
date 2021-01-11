import matplotlib.pyplot as plt

from Random_Walk_Class import RandomWalk

# 只要程序处于活动状态，就不断地模拟随机漫步
while True:
    rw = RandomWalk(90000)   # 创建一个 RandomWalk实例
    rw.fill_walk()      # 执行漫步操作

    # 将所有的点都绘制出来
    plt.style.use('seaborn-darkgrid')
    fig, ax = plt.subplots(figsize=(8, 6))                # *** 调整尺寸：8*6 ***
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=list(point_numbers), cmap=plt.cm.Blues, edgecolors='none' ,s=0.5)

    # *** 突出起点和终点 ***
    ax.scatter(0, 0, c='green', edgecolors='none', s=50)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=50)

    # *** 隐藏坐标轴 ***
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n' or keep_running == 'N':
        print("Random walk has been terminated.")
        break
    elif keep_running == 'y' or keep_running == 'Y':
        print("Processing...")
        continue
    else:
        print("Input Error!")
        break
# end

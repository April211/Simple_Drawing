import matplotlib.pyplot as plt

from Random_Walk_Class import RandomWalk

# 只要程序处于活动状态，就不断地模拟随机漫步
while True:
    rw = RandomWalk()   # 创建一个 RandomWalk实例
    rw.fill_walk()      # 执行漫步操作

    # 将所有的点都绘制出来
    plt.style.use('seaborn-darkgrid')
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s=1, c=rw.y_values, cmap=plt.cm.viridis)
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

import matplotlib.pyplot as plt

squares = [0, 1, 4, 9, 16, 25]  # 定义对应着下标平方的数列（***默认第一个数据点对应的 X坐标值为 0***）
fig, ax = plt.subplots()        # 在一张图片中绘制一个或多个图表
ax.plot(squares, linewidth=2)   # 设置图线的粗细程度

# ***正确设置中文字体***
plt.rcParams['font.sans-serif'] = ['SimHei']

# 设置图表标题、给坐标轴加上标签、设置字体大小
ax.set_title("平方数", fontsize=14)
ax.set_xlabel("值", fontsize=7)
ax.set_ylabel("值的平方", fontsize=7)

# 设置刻度标记的大小
ax.tick_params(axis='both', labelsize=6)

# 打开 Matplotlib查看器并显示绘制图表
plt.show()



"""字体选择 参考：https://blog.csdn.net/lavender_dream/article/details/110181247"""

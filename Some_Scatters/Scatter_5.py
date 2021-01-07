import matplotlib.pyplot as plt

x_values = range(1, 1001)                  # 向 plot函数提供点集的 X坐标值
y_values = [x**3 for x in x_values]        # ***向 plot函数提供点集的 Y坐标值***，使用列表解析法

plt.style.use('seaborn-darkgrid')          # 选择一个合适的绘制样式
fig, ax = plt.subplots()                   # 在一张图片中绘制一个或多个图表

# 根据给定的输入值和输出值绘制散点图，并设置点的粗细程度和颜色（使用颜色映射）
ax.scatter(x_values, y_values, s=1, c=y_values, cmap=plt.cm.viridis)

# 正确设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']

# 设置图表标题、给坐标轴加上标签、设置字体大小
ax.set_title("平方数", fontsize=14)
ax.set_xlabel("值", fontsize=7)
ax.set_ylabel("值的平方", fontsize=7)

# 设置刻度标记的大小
ax.tick_params(axis='both', labelsize=6)

# ***设置每个坐标轴的取值范围：X∈[0, 1100], Y∈[0, 1331000000]***
ax.axis([0, 1100, 0, 1331000000])

# 打开 Matplotlib查看器并显示绘制图表
plt.show()

# 也可以通过下面的代码来实现图表的保存：
# plt.savefig('squares_plot.png', bbox_inches='tight')


"""字体选择 参考：https://blog.csdn.net/lavender_dream/article/details/110181247"""

# 查看内置定义格式：plt.style.available
# 通过在交互式窗口对图像的放大，可以看到单个的点

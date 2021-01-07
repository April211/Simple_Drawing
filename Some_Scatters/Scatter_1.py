import matplotlib.pyplot as plt

plt.style.use('seaborn-darkgrid')
fig, ax = plt.subplots()
ax.scatter(2, 4, s=20)            # ***使用 Scatter方法在指定坐标位置绘制一个点***

# 正确设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']

# 设置图表标题并给坐标轴加上标签
ax.set_title("平方数", fontsize=14)
ax.set_xlabel("值", fontsize=7)
ax.set_ylabel("值的平方", fontsize=7)

# 设置刻度标记的大小
ax.tick_params(axis='both', which='major', labelsize=7)

plt.show()

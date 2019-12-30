import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = list(x**2 for x in x_values)

plt.scatter(x_values, y_values, s=40, c=(0, 0, 0.9), edgecolor="none")

#设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])



plt.show()
import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, edgecolor="none", s=40, c=y_values, cmap=plt.cm.Greens) #使用颜色映射

plt.title("Cubic", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cubic of Value", fontsize=14)

plt.tick_params(axis="both", which="major", labelsize=14)

plt.axis([0, 5100, 0, 126000000000])



plt.savefig("立方.pdf")
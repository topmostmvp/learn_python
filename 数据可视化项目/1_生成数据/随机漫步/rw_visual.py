import matplotlib.pyplot as plt
from random_work import RandomWalk

#只要程序处于活跃状态，就不断的模拟随机漫步
while True:
    #创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk(50000)
    rw.fill_walk()

    #设置绘图窗口的尺寸 
    plt.figure(dpi=1080, figsize=(10, 6)) #dpi为分辨率
    
    #绘制点并将图形显示出来
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, s=1, edgecolor='none')
    
    #突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    
    plt.show() #包含5000个点的随机漫步
    keep_running = input("Make another walk?(y/n:)")
    if keep_running == 'n':
        break
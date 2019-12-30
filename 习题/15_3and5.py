import matplotlib.pyplot as plt
from random import choice

class RandomWalk():
    '''一个生成随机漫步数据的类'''

    def __init__(self, num_points=5000):
        '''初始化随机漫步的属性'''
        self.num_points = num_points

        '''所有随机漫步都始于（0，0）'''
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        '''计算随机漫步包含的所有点'''
        def get_step():
            '''确定每次漫步的距离和方向，并计算这次漫步讲如何移动'''
            direction = choice([1, -1])
            distance = choice([0, 1, 2, 3, 4])
            step = direction * distance
            return step

        #不断漫步，直到列表达到指定的长度
        while len(self.x_values) < self.num_points:
        
            x_step = get_step()
            y_step = get_step()

            '''拒绝原地踏步'''
            if x_step == 0 and y_step == 0:
                continue

            '''计算下一个点的x值和y值'''
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

#只要程序处于活跃状态，就不断的模拟随机漫步
while True:
    #创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk()
    rw.fill_walk()

    #设置绘图窗口的尺寸 
    plt.figure(dpi=1080, figsize=(10, 6)) #dpi为分辨率
    
    #绘制点并将图形显示出来
    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, linewidth=1)
    
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
from random import randint
import pygal

class Die():
    '''表示一个骰子的类'''

    def __init__(self, num_sides=6):
        '''骰子默认六面'''
        self.num_sides = num_sides

    def roll(self):
        """返回一个位于1和骰子面之间的随机数"""
        return randint(1, self.num_sides)


#创建两个D6骰子
die_1 = Die(8)
die_2 = Die(8)

#掷多次骰子，并将结果储存在一个列表中
results = [die_1.roll() +die_2.roll() for roll_num in range(500000)]

#分析结果
max_result = die_1.num_sides +die_2.num_sides
frequencies =[results.count(value) for value in range(2, max_result+1)]

#对结果进行可视化分析
hist = pygal.Bar()  #bar为条形图

hist.title = "Results of rolling D8 + D8 dice 500,000 times."
hist.x_labels = [str(x_label) for x_label in range(2, max_result+1)]

hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D8+D8', frequencies)  #将分析结果添加到图表中
hist.render_to_file('different_dice_visual.svg')
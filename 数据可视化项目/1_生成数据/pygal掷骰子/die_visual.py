from die import Die
import pygal
#创建一个D6
die = Die()

#掷几次骰子，并将结果储存在一个列表中
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

#分析结果
frequencies = []
for value in range(1,die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#对结果进行可视化分析
hist = pygal.Bar()  #bar为条形图

hist.title = "Results of rolling one D6 1000 times"
hist.x_labels = [str(x_label) for x_label in range(1, die.num_sides+1)]
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6', frequencies)  #将分析结果添加到图表中
hist.render_to_file('die_visual.svg')

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

#执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code', r.status_code)

#将API响应存储在一个字典中
response_dict = r.json()
print("Total responsitories:", response_dict['total_count'])

#研究有关仓库的信息
repo_dicts = response_dict['items']
print("Nummber of items:", len(repo_dicts))

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': str(repo_dict['description']),
        'xlink': repo_dict['html_url'] #只有为xlink时链接可以打开
    }
    plot_dicts.append(plot_dict)
    

#可视化
my_style = LS("#336699", base_style=LCS)
my_config = pygal.Config() #创建配置实例
my_config.x_label_rotation = 45 #x轴标签绕x轴旋转45°
my_config.show_legend = False #隐藏图例
my_config.title_font_size = 24 #图表标题字体大小
my_config.label_font_size = 14 #图表副标签字体大小（x轴上的项目名以及y轴上的大部分数字）
my_config.major_label_font_size = 18 #图表主标签字体大小（y轴上为5000整数倍的刻度）
my_config.truncate_label = 15 #将较长的项目缩短为15个字符（鼠标指向时完整显示）
my_config.show_y_guides = False #隐藏表中的水平线
my_config.width = 1000 #自定义宽度

chart = pygal.Bar(my_config, style= my_style)
chart.title = 'Most-stared Python Projects on Github'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos_pygal.svg')
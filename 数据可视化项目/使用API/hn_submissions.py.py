import requests
from operator import itemgetter

#执行API调用并存储响应
ulr = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(ulr)
print(("Status code:"), r.status_code)

#处理有关每篇文章的信息
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids:
    #对于每篇文章，都执行一个API调用
    ulr = ('http://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json')
    submission_r = requests.get(ulr)
    print(submission_r.status_code)
    response_dict = submission_r.json()

    submission_dict = {
        'title': response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        'comments': response_dict.get('descendants', 0),#descendant存在时返回存在值，否则返回指定值（0）
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    print("\ntitle:", submission_dict['title'])
    print("Discussion link:", submission_dict['link'])
    print('Comments:', submission_dict['comments'])
import requests

#执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:java&sort=stars'
r = requests.get(url)
print('Status code', r.status_code)

#将API响应存储在一个字典中
response_dict = r.json()
print("Total responsitories:", response_dict['total_count'])

#研究有关仓库的信息
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

#研究所有仓库
print("\nSelected information adout each repository:")
for repo_dict in repo_dicts:
    print('Name:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print("Stars:", repo_dict['stargazers_count'])
    print("Respository:", repo_dict['html_url'])
    print('Created:', repo_dict['created_at'])
    print('Updted:', repo_dict['updated_at'])
    print('Description:', repo_dict['description'])
    print('\n')

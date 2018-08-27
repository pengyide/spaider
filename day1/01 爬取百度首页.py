import requests

response = requests.get('https://www.baidu.com/')
html = response.content

print(type(html))
print('=========')
print(html)

# 保存页面
with open('baidu.html', 'wb') as bai:
    bai.write(html)

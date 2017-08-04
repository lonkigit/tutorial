import random

import requests


url = "http://txt.bxwxtxt.com/packdown/fulltxt/59/59047.txt"

try:
    book = requests.get(url,timeout=10)
except requests.exceptions.ConnectionError:
    print('当前小说无法下载')

filename = '/home/lonki/pythonspider/books/%s.txt' % 'test1'
with open(filename,'wb') as f:
    f.write(book.content)
    f.close()
print("下载完成")
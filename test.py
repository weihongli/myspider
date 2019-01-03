import json
import requests

#Content = "计算机网络"


#"""https://so.csdn.net/so/search/s.do?q=%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1%E8%AF%AD%E8%A8%80%E7%9A%84%E5%88%86%E7%B1%BB&t=&o=&s=&l="""

#url = 'https://www.jianshu.com/search/do?q=' + Content + '&type=note&page=' + str(1) + '&order_by=default'
#url = "https://so.csdn.net/so/search/s.do?q=%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1%E8%AF%AD%E8%A8%80%E7%9A%84%E5%88%86%E7%B1%BB&t=&o=&s=&l="
#headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:49.0) Gecko/20100101 Firefox/49.0'}
#page = requests.get(url=url, headers=headers)
#json_data = json.loads(page.text)
# with open("1.html", "w", encoding="utf-8") as file:
# 	print(page.content, file=file)

from MysqlClass import Mysql
from Settings.DBSettings import DATABASES

host = DATABASES['default']['HOST']
user = DATABASES['default']['USER']
passwd = DATABASES['default']['PASSWORD']
db = DATABASES['default']['NAME']
port = DATABASES['default']['PORT']
Mysql()

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:49.0) Gecko/20100101 Firefox/49.0'}

html = requests.get("https://www.jianshu.com/p/46d260f1a974")
print(html.text)



import csdn_spider
from MysqlClass import Mysql
from Settings.DBSettings import DATABASES


url = "https://so.csdn.net/so/search/s.do?"


host = DATABASES['default']['HOST']
user = DATABASES['default']['USER']
passwd = DATABASES['default']['PASSWORD']
db = DATABASES['default']['NAME']
port = DATABASES['default']['PORT']
mysql = Mysql(host=host, user=user, passwd=passwd, db=db, port=port)
result = mysql.find_data("scatalog")

for i in result:
	print(i[2])
	for p in range(3):
		data = {"q": i[2], "t": "blog", "p": p + 1}
		title, href = csdn_spider.getpage(url, datadict=data)
		csdn_spider.save2db(url, title, href, i[0])


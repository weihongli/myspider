import csdn_spider
from MysqlClass import Mysql
from Settings import Configuration

page = Configuration.PAGE

mysql = Mysql()
result = mysql.find_data("scatalog")

for i in result:
	print(i[2])
	for p in range(page):
		data = {"q": i[2], "t": "blog", "p": p + 1}
		title, href = csdn_spider.getpage(datadict=data)
		csdn_spider.save2db(title, href, i[0])

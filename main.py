import csdn_spider
from MysqlClass import Mysql
from Settings import Configuration
import jianshu_spider

PAGE = Configuration.PAGE

if __name__ == '__main__':
	mysql = Mysql()
	scatalog = mysql.find_data("scatalog")
	# 先利用关键词搜索功能从csdn上爬取内容
	if scatalog is None:
		print("未查询到次级目录")
		exit(0)

	for i in scatalog:
		for p in range(PAGE):
			data = {"q": i[2], "t": "blog", "p": p + 1}
			title, href = csdn_spider.getpage(datadict=data)
			csdn_spider.save2db(title, href, i[0])
	# 再利用关键词搜索功能从简书上爬取内容
	for i in scatalog:
		for p in range(PAGE):
			data = {"q": i[2], "type": "note", "page": p+1, "order_by": "default"}
			mydict = jianshu_spider.get_json_resultlist(data)
			if mydict is not None:
				jianshu_spider.save2db(mydict, i[0])

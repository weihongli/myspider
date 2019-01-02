import requests
import time
from lxml import etree
from MysqlClass import Mysql
from Settings.DBSettings import DATABASES


def getpage(url, datadict):
	time.sleep(1)
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:49.0) Gecko/20100101 Firefox/49.0'}
	page = requests.get(url, params=datadict, headers=headers).text
	page = page.replace("<em>", "")
	page = page.replace("</em>", "")
	html = etree.HTML(page)
	result_href = html.xpath("//div[@class='limit_width']/a[1]/@href")
	result_title = html.xpath("//div[@class='limit_width']/a[1]/text()")
	return result_title, result_href


def save2db(url, titlelist, hreflist, scatalogid):
	if len(titlelist) != len(hreflist):
		return None
	host = DATABASES['default']['HOST']
	user = DATABASES['default']['USER']
	passwd = DATABASES['default']['PASSWORD']
	db = DATABASES['default']['NAME']
	port = DATABASES['default']['PORT']
	mysql = Mysql(host=host, user=user, passwd=passwd, db=db, port=port)
	for i in range(len(titlelist)):
		datadict = {"title": titlelist[i],
					"href": hreflist[i],
					"scatalogid": scatalogid,
					"fullcontent": getmaincontenthtml(hreflist[i]),
					"content": ""}
		mysql.insert_data_to_pages(my_dict=datadict)


def getmaincontenthtml(url):
	page = requests.get(url).text
	html = etree.HTML(page)
	result = html.xpath("//div[@id='article_content']")
	ans = ""
	for i in result:
		tmp = etree.tostring(i,encoding="utf-8")
		ans += tmp.decode("utf-8").replace("&lt;", "<").replace("&gt;", ">").replace(" ", "")
	return ans

import requests
import time
from lxml import etree
from Utils.MysqlClass import Mysql
import Utils.utils as utils


def getpage(datadict):
	"""
		根据数据字典获取页面，然后分析页面，返回结果
	:param datadict: 数据字典 传入爬虫的参数数据
	:return: 返回两个列表，第一个是标题列表 第二个是链接列表
	"""
	url = "https://so.csdn.net/so/search/s.do?"
	time.sleep(1)
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:49.0) Gecko/20100101 Firefox/49.0'}
	page = requests.get(url, params=datadict, headers=headers).text
	page = page.replace("<em>", "")
	page = page.replace("</em>", "")
	html = etree.HTML(page)
	result_url = html.xpath("//div[@class='limit_width']/a[1]/@href")
	result_title = html.xpath("//div[@class='limit_width']/a[1]/text()")
	return result_title, result_url


def save2db(titlelist, urllist, scatalogid):
	"""

	:param titlelist: 标题列表
	:param urllist: 链接列表
	:param scatalogid: 二级目录的id
	:return: 无返回值
	"""
	if len(titlelist) != len(urllist):
		return None
	mysql = Mysql()
	for i in range(len(titlelist)):
		datadict = {"title": titlelist[i].encode("utf-8"),
					"href": urllist[i].encode("utf-8"),
					"scatalogid": scatalogid,
					"fullcontent": getmaincontenthtml(urllist[i]).encode("utf-8"),
					"content": getmaincontent(urllist[i]).encode("utf-8")}
		mysql.insert_data_to_pages(my_dict=datadict)


def getmaincontenthtml(url):
	"""

	:param url:
	:return:
	"""
	page = requests.get(url).text
	html = etree.HTML(page)
	result = html.xpath("//div[@id='content_views']")
	ans = ""
	for i in result:
		tmp = etree.tostring(i, encoding="utf-8")
		tmp = tmp.decode("utf-8").replace("&lt;", "<").replace("&gt;", ">")
		tmp = utils.dealstring(tmp)
		ans += tmp
	return ans


def getmaincontent(url):
	"""

	:param url:
	:return:
	"""
	page = requests.get(url).text
	html = etree.HTML(page)
	result = html.xpath("//div[@id='content_views']")
	if result is None or len(result) <= 0:
		return ""
	tmp = result[0].xpath("string(.)")
	tmp = utils.dealstring(tmp)
	return tmp

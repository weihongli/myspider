import requests
from lxml import etree
from collections import OrderedDict
import Utils.utils as utils
from Utils.MysqlClass import Mysql
import json
import time

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:49.0) Gecko/20100101 Firefox/49.0'}


def get_json_resultlist(datadict):
    base_url = 'https://www.jianshu.com/search/do?'
    # data = urllib.parse.urlencode(datadict)
    time.sleep(3)
    html = requests.post(base_url, data=datadict, headers=headers).text
    result = json.loads(html, encoding="utf-8")
    if "error" in result.keys():
        return None
    else:
        return result


def save2db(mydict, scatalogid):
    article = OrderedDict()
    for tag in mydict['entries']:
        article['title'] = utils.dealstring(etree.HTML(tag['title']).xpath("string(.)"))
        article['scatalogid'] = scatalogid
        article['href'] = "https://www.jianshu.com/p/" + tag["slug"]
        article['fullcontent'] = getmaincontenthtml(article['href'])
        article['content'] = getmaincontent(article['href'])
        mysql = Mysql()
        mysql.insert_data_to_pages(article)


def getmaincontenthtml(url):
    page = requests.get(url, headers=headers).text
    html = etree.HTML(page)
    result = html.xpath("//div[@class='show-content']")
    ans = ""
    for i in result:
        tmp = etree.tostring(i, encoding="utf-8")
        tmp = tmp.decode("utf-8").replace("&lt;", "<").replace("&gt;", ">")
        tmp = utils.dealstring(tmp)
        ans += tmp
    # print(ans)
    return ans


def getmaincontent(url):
    page = requests.get(url, headers=headers).text
    html = etree.HTML(page)
    result = html.xpath("//div[@class='show-content']")
    if result is None or len(result) <= 0:
        return ""
    tmp = result[0].xpath("string(.)")
    tmp = utils.dealstring(tmp)
    # print(tmp)
    return tmp

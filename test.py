from crawler import downloadhtml
import urllib

file = open("./1.html", "w", encoding="utf8")
word = '周杰伦'
url = 'http://www.baidu.com.cn/s?wd=' + urllib.parse.quote(word) + '&pn=0'
# word为关键词，pn是百度用来分页的..
str = "123"

result = downloadhtml(url)
result.encode("utf8")
print(result, file=file)

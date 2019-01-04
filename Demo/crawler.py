import urllib.request


def downloadhtml(url, user_agent="Mozilla/5.0", trytimes=3):
	print("Downloading!")
	headers = {"User-agent": user_agent, 'Accept': 'application/json'}
	request = urllib.request.Request(url, headers=headers)
	try:
		html = urllib.request.urlopen(request).read()
		html = html.decode("utf-8")
	except urllib.request.URLError as e:
		print(e.reason)
		html = None
		if trytimes > 0:
			if hasattr(e, 'code') and 500 <= e.code < 600:
				downloadhtml(request, trytimes-1)
	return html

"""https://www.jianshu.com/search?q=软件工程&page=1&type=note"""
data = bytes(urllib.parse.urlencode({'q': '软件工程', 'page': '1', 'type': 'note', 'order_by': 'default'}), encoding='utf8')

with open("1.html", "w", encoding="utf-8") as file:
	print(downloadhtml("https://so.csdn.net/so/search/s.do?q=%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1%E8%AF%AD%E8%A8%80%E7%9A%84%E5%88%86%E7%B1%BB&t=&o=&s=&l="),file=file)
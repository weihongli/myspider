import urllib.request


def downloadhtml(url, user_agent="Mozilla/5.0", trytimes=2):
	print("Downloading!")
	headers = {"User-agent": user_agent}
	request = urllib.request.Request(url, headers=headers)
	try:
		html = urllib.request.urlopen(request).read().decode("utf-8")
	except urllib.request.URLError as e:
		print(e.reason)
		html = None
		if trytimes > 0:
			if hasattr(e, 'code') and 500 <= e.code < 600:
				downloadhtml(request, trytimes-1)
	return html

print(downloadhtml("https://www.qidian.com/rank/signnewbook?chn=21&style=2&page=1"))
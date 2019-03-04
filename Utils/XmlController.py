from bs4 import BeautifulSoup

def deal_img_jianshu(content):

	soup = BeautifulSoup(content, features="lxml")
	for i in soup.find_all("img", attrs={'src': True}):
		tmp = i['src']
		if tmp[0] != 'h':
			i['src'] = tmp[2:]
	print(soup)
	return str(soup)


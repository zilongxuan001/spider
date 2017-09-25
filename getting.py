#coding=utf-8
import urllib.request
import re

def getHtml(url):
	page = urllib.request.urlopen(url)
	htmlbytes = page.read()
	html=htmlbytes.decode('utf-8')
	return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl,'%s.jpg' % x)
        x+=1


html = getHtml("http://tieba.baidu.com/p/2460150866")

print(getImg(html))

#python2可以直接urllib.urlopen。python3改成了urllib.request.urlopen

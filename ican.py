# -*- coding: utf-8 -*-
import pytesseract
from PIL import Image,ImageEnhance
import requests
import os,sys
import re
import IPGen
from threading import Thread
import cStringIO
from color import tobw

def vote():
	s = requests.Session()
	#ra = s.get('http://ican.cdstm.cn/index.php?m=Vote&a=votedetail&code=1708')
	pic_url = "http://ican.cdstm.cn/index.php?m=Common&a=GetCode&randcode=0.23211031639948487"
	r = s.get(pic_url,timeout=50)
	ps = r.headers['set-cookie'].split(';')[0]
	while True:
		pic_url = "http://ican.cdstm.cn/index.php?m=Common&a=GetCode&randcode=0.23211031639948487"
		try:
			r = s.get(pic_url,timeout=50)
		except:
			continue
		pic = cStringIO.StringIO(r.content)
		im = tobw(Image.open(pic))
		#im.show()
		#im1 = im.crop((5,6,23,18))
		#im2 = im.crop((45,6,63,18))
		#im = Image.open(pic)
		#im = ImageEnhance.Contrast(im.convert('L')).enhance(20)
		#ps = r.headers['set-cookie'].split(';')[0]
		#with open('vcode.png', 'wb') as pic:
			#pic.write(r.content)
		try:
			im = pytesseract.image_to_string(im)
			#im1 = pytesseract.image_to_string(im1)
			#im2 = pytesseract.image_to_string(im2)
		except:
			continue
		im = im.replace(' ', '')
		number = re.findall(r"[0-9]*",im)
		sumn = 0
		for i in number:
			if i != '':
				sumn = sumn + int(i)
		if sumn == 0:
			continue
		ip=IPGen.IPGen().ip()
		headers = {'Host': 'ican.cdstm.cn',
		'Connection':'keep-alive',
		'Content-Length': 20,
		'Accept': '*/*',
		'Origin': 'http://ican.cdstm.cn',
		'X-Requested-With': 'XMLHttpRequest',
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
		'Content-Type': 'application/x-www-form-urlencoded',
		'Referer': 'http://ican.cdstm.cn/index.php?m=Vote&a=votedetail&code=1708',
		'Accept-Encoding': 'gzip, deflate',
		'X-Forwarded-For':ip,
		'Accept-Language': 'zh-CN,zh;q=0.8',
		'Cookie':ps
		}
		try:
			p = s.post('http://ican.cdstm.cn/index.php?m=Vote&a=vote',headers = headers,data={'code':'1708', 'captcha':sumn},timeout=50)
		except:
			continue
		print p.text
thread_list = list()
for i in range(20):
	thread_list.append(Thread(target=vote, args=()))
for thread in thread_list:   
        thread.start()

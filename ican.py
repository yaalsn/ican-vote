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
from collect import to10

d0 = '00011000001111000110011011000011110000111100001111000011011001100011110000011000'
d1 = '00011000001110000111100000011000000110000001100000011000000110000001100001111110'
d2 = '00111100011001101100001100000011000001100000110000011000001100000110000011111111'
d3 = '01111100110001100000001100000110000111000000011000000011000000111100011001111100'
d4 = '00000110000011100001111000110110011001101100011011111111000001100000011000000110'
d5 = '11111110110000001100000011011100111001100000001100000011110000110110011000111100'
d6 = '00111100011001101100001011000000110111001110011011000011110000110110011000111100'
d7 = '11111111000000110000001100000110000011000001100000110000011000001100000011000000'
d8 = '00111100011001101100001101100110001111000110011011000011110000110110011000111100'
d9 = '00111100011001101100001111000011011001110011101100000011010000110110011000111100'

fuck_list ={d0:0,d1:1,d2:2,d3:3,d4:4,d5:5,d6 :6,d7:7,d8:8,d9:9}

wired = '00000000000000000000000000000000000000000000000000000000000000000000000000000000'

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
		key1 = to10(im,5,7,12,16)
		key2 = to10(im,14,7,21,16)
		key3 = to10(im,45,7,52,16)
		key4 = to10(im,54,7,61,16)
		sumn = 0
		if key2!=wired and key4!= wired:
			sumn = fuck_list[key1] *10 + fuck_list[key2] + fuck_list[key3] *10 + fuck_list[key4]
		if key2 == wired and key4 == wired:
			sumn = fuck_list[key1] + fuck_list[key3]
		if key2 == wired and key4 != wired:
			sumn = fuck_list[key1] + fuck_list[key3]*10 + fuck_list[key4]
		if key2 != wired and key4 == wired:
			sumn = fuck_list[key1]*10 + fuck_list[key2] + fuck_list[key3]
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

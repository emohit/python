# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 18:58:53 2016

@author: monarang
"""

from bs4 import BeautifulSoup
from PIL import Image
import requests
from StringIO import StringIO

s = requests.Session()
first_page = s.get("http://www.bsesdelhi.com/bsesdelhi/caVerification4Pay.do")

hed ={
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'en-US,en;q=0.8,hi;q=0.6',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Content-Length':'53',
'Content-Type':'application/x-www-form-urlencoded',
'Cookie':first_page.headers['set-cookie'].split(';')[0]+'; _gat=1; _ga=GA1.2.198875373.1472635208; '+first_page.headers['set-cookie'].split(';')[1].split(',')[1],
'Host':'www.bsesdelhi.com',
'Origin':'http://www.bsesdelhi.com',
'Referer':'http://www.bsesdelhi.com/bsesdelhi/caVerification4Pay.do',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}

r = s.get('http://www.bsesdelhi.com/bsesdelhi/simpleCaptcha')
i = Image.open(StringIO(r.content))
i.show()

payload = {'txtCA_Number':'101684880','answer':'43ww7','caller':'instantPay'}

post_page = s.request('POST','http://www.bsesdelhi.com/bsesdelhi/caVerf4PayInstantpay.do?parameter=getUserDetails',data = payload,headers=hed)

post_page.content

soup = BeautifulSoup(post_page.content)

try:
    mob_value = soup.find('input', {'id': 'idmobile'}).get('value')
    email_value = soup.find('input', {'id': 'idmail'}).get('value')
except:
    pass


hed2 ={
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'en-US,en;q=0.8,hi;q=0.6',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Content-Length':'116',
'Content-Type':'application/x-www-form-urlencoded',
'Cookie':'_gat=1; '+ first_page.headers['set-cookie'].split(';')[0]+'; _ga=GA1.2.198875373.1472635208; '+first_page.headers['set-cookie'].split(';')[1].split(',')[1],
'Host':'www.bsesdelhi.com',
'Origin':'http://www.bsesdelhi.com',
'Referer':'http://www.bsesdelhi.com/bsesdelhi/caVerf4PayInstantpay.do?parameter=getUserDetails',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}

payload2 = {'txtCA_Number':'101684880','txtCA_Number':'101684880','idmobile':mob_value,'idcompCode':'BRPL','consMobileNo':'','consEmailID':'','caller':''}

post_page2 = s.request('POST','http://www.bsesdelhi.com/bsesdelhi/caVerf4PayInstantpay.do?parameter=getUserBillDetails',data = payload2,headers=hed2)

soup2 = BeautifulSoup(post_page2.content)

try:
    e=''
    name = soup2.find('div', class_='tc1 txtCen').text.split(':')[1]
    for i in soup2.findAll('div', class_='tc3 fleft'):
        e+=i.text+';'

except:
    pass

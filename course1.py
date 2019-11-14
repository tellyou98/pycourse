#!/usr/bin/env python
#encoding: utf-8
#coding: utf-8
import sys
import requests
import pyquery
import re

key_word = { 'wd' : 'dingzw'}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
response = requests.get("http://www.baidu.com/s?",params=key_word, headers = headers)
html = pyquery.PyQuery(response.text)
for res_item in html('.result'):
  myres = pyquery.PyQuery(res_item)('a')
  print (myres.text())
  # print(myres)
  print(myres.attr('href'))

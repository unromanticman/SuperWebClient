#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# python 2.7.11

from SuperWebClient import SuperWebClient 


client = SuperWebClient()

#Set Header

client.setHeader('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')
client.setHeader('Referer','http://{YOUR_URL}/')

#POST

data = {'user_login': '123', 'user_pass': '123'}
rs = client.UploadValues('http://{YOUR_URL}',data)
print rs

#GET
rs = client.DownloadString('http://{YOUR_URL}/')
print rs

client.clean()


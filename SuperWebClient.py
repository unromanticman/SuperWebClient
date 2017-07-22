#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# python 2.7.11

import requests

class SuperWebClient:

    def __init__(self):
		self._cookies  = {}
		self._headers  = {}

    def UploadValues(self,url,_data):
		try:
			r = requests.post(url,headers=self._headers,data=_data,cookies=self._cookies)
			for cookie in r.cookies:
				self.setCookie(cookie.name,cookie.value)   		
			return r.text
		except:
		    return "[Failed] UploadValues , url = " + url
    	
    def DownloadString(self,url):
		try:
			r = requests.get(url,headers=self._headers,cookies=self._cookies)
			for cookie in r.cookies:
				self.setCookie(cookie.name,cookie.value)   		
			return r.text
		except:
		    return "[Failed] DownloadString , url = " + url

    def setHeader(self,key,value):
    	self._headers[key] = value
    def setCookie(self,key,value):
    	self._cookies[key] = value
    def getCookie(self):
    	return self._cookies
    def clean(self):
    	self._cookies  = {}
    	self._headers  = {}


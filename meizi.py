#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import os
from download import request
from pymongo import MongoClient
import datetime

class Meizitu():

	def __init__(self):
		client = MongoClient()
		db = client['meinvxiezhen']#c创建一个数据库
		self.meizitu_collection = db['meizitu']#在meizixiezhenji这个数据库中，创建一个集合
		self.title = '' #页面主题
		self.url = '' #页面地址
		self.img_urls = []#所有图片的url地址

	global currentPath,headers
	headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
	currentPath = os.path.abspath('.')

	def all_url(self,url):
		Soup = self.requestlxml(url)
		li_list = Soup.find('ul',id = 'pins').find_all('li')
		for li in li_list:
			all_a = li.find('span',class_ = None).find_all('a')
			for a in all_a:
				title = a.get_text()
				href = a['href']
				self.title = title#主题的title给self.title
				self.url = href #  
				isok = self.mkdir(title)
				if self.meizitu_collection.find_one({'主题页面':href}):
					print('页面已经爬取过了')	
				else: #如果没有爬取就要去爬取了
					html_Soup = self.requestlxml(href)
					max_span = html_Soup.find('div',class_ = 'pagenavi').find_all('span')[-2].get_text()
					print(title,isok,max_span)
					for page in range(int(max_span)+1):
						page_url = href + '/' + str(page)
						self.img_urls.append(page_url)
						self.img(page_url)#保存图片
						if int(max_span)==page:
							post = {
								'标题':self.title,
								'主题页面':self.url,
								'图片地址':self.img_urls,
								'获取时间':datetime.datetime.now()
							}
							self.meizitu_collection.save(post)#写入数据库
							print('写入数据库成功')

	def requestlxml(self,url):
		content = request.get(url,5)
		content_Soup = BeautifulSoup(content.text,'lxml')
		return content_Soup
	
	def mkdir(self,path):
		path = path.strip()
		mypath = os.path.join(currentPath,'meizi')
		isExists = os.path.exists(os.path.join(mypath,path))
		if not isExists:
			os.makedirs(os.path.join(mypath,path))
			os.chdir(os.path.join(mypath,path))
			return True
		else:
			os.chdir(os.path.join(mypath,path))
			return False

	def img(self,page_url):
		image_Soup = self.requestlxml(page_url)
		image_url = image_Soup.find('div',class_ = 'main-image').find('img')['src']
		self.save_img(image_url)


	def save_img(self,image_url):
		name = image_url[-9:]
		img = request.get(image_url,5)
		f = open(name,'ab')
		f.write(img.content)
		f.close()
		print('保存完毕:%s' % (image_url))



meizitu = Meizitu()

meizitu.all_url('http://www.mzitu.com/xinggan/page/18')






import os, random, time, sys
from selenium import webdriver
from bs4 import BeautifulSoup
from Connection import Connection
browser=webdriver.Chrome("C:\\Users\\EDS\\Desktop\\chromedriver.exe")
class WebScraping:
    def __init__(self,dbName,collectionName,websiteUrl):
        self.connection=Connection(dbName,collectionName)
        self.url=websiteUrl
        
    def go_to_url(self,url):
        return browser.get(url)
    
    def forum (self):
        browser.find_element_by_id(self.connection.getCollection()).click()
    
    def subjects(self):
        self.refreshBrowser()
        div=soup.find_all('li',{'class':'row'})
        dict={}
        for i in div:
            subject=i.find('a').get_text().strip()
            url=i.find('a')['href']
            dict.update({subject:url})
        return dict
    def refreshBrowser(self):
        src=browser.page_source
        soup=BeautifulSoup(src,'lxml')
        
    def scrapingOne(self):
        for url in self.subjects().values():
            browser.get(url)
            div1=[]
            end=self.get_number_topics()
            pageNumber=1
            while(pageNumber<=end):
                self.refreshBrowser()
                li=soup.find_all('li',{'class':'row bg2 sticky'})+soup.find_all('li',{'class':'row bg1 sticky'})+soup.find_all('li',{'class':'row bg1'})+soup.find_all('li',{'class':'row bg2'})
                d=soup.find('div',{'class':'pagination'})
                d1=d.find('span')
                pages={}
                d2=d1.find_all('a')
                for i in d2:
                    pages.update({i.get_text():i['href']})
                for i in li:
                    topic=i.find('a').get_text().strip()
                    topicUrl=i.find('a')['href']
                    author=i.findAll('a')[1].get_text().strip()
                    views=i.find('dd',{'class':'views'}).get_text().strip()
                    self.connection..insert_one({'subject':'Members Corner','topic':topic,'topicUrl':topicUrl,'views':views})
                    div1.append(topicUrl)# div1 contains the different topics 
                pageNumber=pageNumber+1
                browser.get(pages[str(pageNumber)])
                return div1
    def get_number_topics(self):
        self.refreshBrowser()
        div2=soup.find('div',{'class':'pagination'})#div2 contains the content of one topic from div1
        div3=div2.find_all('strong')
        return int(div3[-2].get_text())
        
    def scrapingTwo(self):
        div1=self.scrapingOne()
        for i in div1:
        try:

            url1=i
            browser.get(url1)
            myquery = {'topicUrl':url1} 
            src=browser.page_source
            soup=BeautifulSoup(src,'lxml')
            div3=soup.find_all('div',{'class':'content'})#div3 is for the content of the topic
            newvalues = {"$set":{'content':div3[0].get_text().strip()}}
            collection.update_one(myquery, newvalues)
            for i in range(1,len(div3)):
                newvalues = {"$push":{'comments':div3[i].get_text().strip()}}

                self.connection().update_one(myquery, newvalues)
        except:
            continue



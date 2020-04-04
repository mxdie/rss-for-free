import importlib
import time 
from .pt_rss import rss
import json
from urllib import request
import sys
import os
from rss_for_free.settings import *

class rss_for_free():
    # 初始化
    def __init__(self):
        #导入配置文件 
        
        with open(CONFIG_PATH,'r') as f:
            self.config = json.load(f)
            
    # 运行
    def run(self, sites: tuple):
        #导入历史下载数据
        dlHistory = [set() for i in range(len(sites))]
        with open(HISTORY_PATH, 'r') as f:
            for line in f:
                _site,_id = line.split()
                if _site in sites:
                    dlHistory[sites.index(_site)].add(_id)
        tryNum = [0 for i in range(len(sites))]
        while 1:
            for i in range(len(sites)):
                # 限制导入模块儿失败次数
                if tryNum[i]<3:
                    site = sites[i]
                else:
                    break
                curConfig = self.config[site]
                # 获取rss信息
                try:
                    rssInfo = rss(curConfig['rsslink']).getinfo()
                    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'  '+site+'rss成功')
                except:
                    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'  '+site+'rss失败')
                    break
                # 去掉已经下载的种子
                for _id in list(rssInfo):
                    if _id in dlHistory[i]:
                        del rssInfo[_id]

                # 导入模块
                
                try:
                    curSite = importlib.import_module('rss_for_free.sites.'+site).func(rssInfo, curConfig)
                except:
                    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'  '+'导入'+site+'模块失败')
                    tryNum[i] += 1
                    if tryNum[i] == 3:
                        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'  '+'放弃导入'+site+'模块')
                    break

                
                # 模块内部筛选
                
                
                try:
                    curSite.fitRule()
                    rssInfo = curSite.rssInfo
                except:
                    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'  '+site+'内部筛选失败')
                    break
                
                # 下载
                dlUrl = curConfig['dlurl']
                dlPath = curConfig['dlpath']
                dledList = self.dlTor(dlUrl,rssInfo,dlPath)
                
                # 记录已下载
                dlHistory[i].update(dledList)
                with open(HISTORY_PATH, 'a') as f:
                    for _id in dledList:
                        f.write(site+' '+_id+'\n')
            time.sleep(int(self.config['common']['sleep']))
    
    def dlTor(self,dlUrl:str , rssInfo:str ,dlPath: str):
        downloaded = []
        opener = request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36')]
        request.install_opener(opener)
        for tor_id in list(rssInfo):
            bt_link= dlUrl.format(id=tor_id)
            maxtyies = 6
            for tyies in range(1,maxtyies):
                try:
                    request.urlretrieve(bt_link,dlPath+tor_id+'.torrent')
                    downloaded.append(tor_id)
                    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'  '+"ID:{}下载成功 TITLE:{}".format(tor_id,rssInfo[tor_id]))
                    break     
                except:
                    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'  '+tor_id+'下载失败，重试第'+str(tyies)+'次中')
                    if tyies == 5:
                        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'  '+'GG,下一个')          
        return downloaded

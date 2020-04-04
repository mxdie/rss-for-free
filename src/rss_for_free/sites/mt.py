import re
import json
from urllib import request
import time
class func():
    def __init__(self,rssInfo: dict, curConfig: dict):
        self.rssInfo = rssInfo
        self.curConfig = curConfig
        self.sizerule = ["KB","MB","GB","TB"]
    def fitRule(self):
        self.fitSize()
        self.fitFree()
    def fitFree(self):
        if not self.rssInfo: return
        pagelink = 'https://pt.m-team.cc/details.php?id='
        cookies = self.curConfig["cookie"]
        for tor_id in list(self.rssInfo):
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'  '+tor_id+'查询优惠')
            id_link= pagelink+tor_id
            headers= {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
                    'cookie':cookies}
            maxtyies = 6
            for tyies in range(1,maxtyies):
                try:
                    id_request=request.Request(url=id_link,headers=headers)
                    html=request.urlopen(id_request,timeout=30).read().decode('utf-8','ignore')
                    title=re.findall('<h1 align="center" id="top">(.+?)</h1>',html)[0]
                    try:
                        youhui = re.findall('<b>(.+?)</b>',title)[0]
                    except:
                        youhui = ''
                    if 'free' not in youhui:
                        del self.rssInfo[tor_id]
                    break
                except:
                    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'  '+tor_id+'查询free失败，重试第'+str(tyies)+'次中')
                    if tyies == 5:
                        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'  '+'GG,下一个')
                        del self.rssInfo[tor_id]
                    continue

    def fitSize(self):
        for _id in list(self.rssInfo):
            tor_title = self.rssInfo[_id][::-1]
            ind = tor_title.index('[')
            #title = tor_title[ind+1:][::-1]
            size = tor_title[1:ind][::-1].split()
            size = float(size[0])*10**((self.sizerule.index(size[1])-2)*3)
            if int(self.curConfig['sizemin'])<=size<= int(self.curConfig['sizemax']):
                pass
            else:
                del self.rssInfo[_id]
from xml.etree import ElementTree
from urllib import request
from io import BytesIO
import json
import time
class rss():
    def __init__(self,rssLink):
        self.rss_link = rssLink
    def getinfo(self):
        maxtry = 6
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
        for tyies in range(1,maxtry):
            try:
                rss_html = request.Request(url = self.rss_link,headers = headers)
                f = BytesIO(request.urlopen(rss_html,timeout=30).read())
                break
            except:
                print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'  '+'rss网络连接失败，重试第'+str(tyies)+'次中')
                if tyies == 5:
                    print('GG')
                    return {}
                continue
        tree = ElementTree.parse(f)
        f.close() 
        row = 0
        res = {}
        for emement in tree.getiterator():
            if emement.tag == 'item':
                row+=1
            if row>0:
                if emement.tag == 'title':
                    tor_title = emement.text
                if emement.tag == 'link':
                    tor_id   = emement.text.split('=')[1]
                    res[tor_id] = tor_title
                    row -= 1
        return res
if __name__ == "__main__":
    print(rss('https://pt.m-team.cc/torrentrss.php?https=1&rows=10&isize=1').getinfo())
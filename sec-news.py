# coding:utf-8
import sys, requests, re
from bs4 import BeautifulSoup


def geturl():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    x = 0
    for i in range(1,113,1):
        url = 'http://wiki.ioin.in/page-%d' %(i)
        print '现在开始第%d页的抓取' %(i)
        req = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(req.text, 'lxml')
        res = soup.find_all(href=re.compile('/url/'))
        # for x in soup.body.tbody.stripped_strings :

        for r in res:
            try:

                encodeurl = 'http://wiki.ioin.in' + r['href']
                h = requests.get(encodeurl, headers=headers, timeout=10)
                realurl = h.url
                code = h.status_code
                print code
                print('第%d条信息链接为:%s' % (x + 1, realurl))
                realtitle = r.contents[0].strip()
                print('第%d条信息标题为:%s' % (x + 1, realtitle))
                with open('secnews.txt', 'a') as f:
                    f.write(realurl + " | " + realtitle + '\n')
                x += 1
            except:
                badurl='http://wiki.ioin.in' + r['href']
                with open('bad.txt','a') as f:
                    f.write(badurl+'\n')
                print('httperror %d' %(x+1))
                x += 1
                continue






if __name__ == '__main__':
    geturl()
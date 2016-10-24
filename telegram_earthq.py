#!-#-coding: utf8-*-

import time
import requests
import json
import urllib2
from bs4 import BeautifulSoup
import telepot

TOKEN = '293857084:AAEXAHPdUAv-irNRQEfkrBM5MFnInD4gS0o'
bot = telepot.Bot(TOKEN)
lasttime = ""

def earthq():
    try:
        url = 'http://www.kma.go.kr/weather/earthquake_volcano/report.jsp'
        handle = urllib2.urlopen(url)
        data = handle.read()
        soup = BeautifulSoup(data, 'html.parser' )
        
        table = soup.find("table")
        rows = table.find_all("td")
        
        #강도 
        size = str(rows[0])
        size2 = size.replace("""<td class=""><strong>""", "")
        size3 = size2.replace("</strong></td>", "")
        print size3
        
        #날짜 
        date = str(rows[1])
        date2 = date.replace("<td>", "")
        date3 = date2.replace("</td>", "")
        print date3
        
        #진앙
        local = str(rows[2])
        local2 = local.replace("<td>", "")
        local3 = local2.replace("</td>", "")
        print local3
        
        #사유
        why = str(rows[3])
        why2 = why.replace("<td>", "")
        why3 = why2.replace("</td>", "")
        print why3
        
        result =[date3, local3, size3, why3]
    except:
        result = [0,0,0,0]
    return result
 
while True:
    time.sleep(30)
    result = earthq()
    if result[0] == 0:
        print('오늘자 관측없음')
       
        continue    
    elif lasttime == "":
        lasttime = result[0]
        print "비어있음"
        continue
        
    elif lasttime == result[0]:
        print "다른점 없음"
        continue
    
    
    elif lasttime != result[0]:
                lasttime = result[0]
                bot.sendMessage('18311619', "[지진안내]\n%s\n지역: %s\n진도: %s\n원인: %s" %(result[0], result[1], result[2], result[3]))
                time.sleep(360)
                continue
        
    else:
        continue    
    
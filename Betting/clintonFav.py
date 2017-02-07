#clintonFav.py
#Keeps track of Clinton's favorabilty polling average

import requests, bs4, time, textmyself, webbrowser

def makeBank(url, htmlClass):
    page = requests.get(url)
    page.raise_for_status()
    pageSoup = bs4.BeautifulSoup(page.text, "html.parser")
    elems = pageSoup.select('.' + htmlClass)
    return elems

updated = False
tags = makeBank('http://www.realclearpolitics.com/epolls/other/clinton_favorableunfavorable-1131.html', 'rcpAvg')
toParse = tags[0].getText()

index = 0
avg = toParse[index:index+2]
while avg != '--':
    index += 1
    avg = toParse[index:index+2]
index += 2
avg = toParse[index:index+4]
print('Cur avg is: ' + avg)

while not updated:
    newTags = makeBank('http://www.realclearpolitics.com/epolls/other/clinton_favorableunfavorable-1131.html', 'rcpAvg')
    curAvg = newTags[0].getText()
    curAvg = curAvg[index: index + 4]
    if avg != curAvg:
        toText = 'NEW POLL:\nOld dirOfC was ' + avg + '\nNew dirOfC is ' + curAvg
        webbrowser.open('https://www.predictit.org/')
        webbrowser.open('http://www.realclearpolitics.com/epolls/other/clinton_favorableunfavorable-1131.html')
        textmyself.textmyself(toText)
        updated = True
    time.sleep(5)

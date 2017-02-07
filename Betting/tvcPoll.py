#tvcPoll.py
#Monitors Trump vs Clinton polling
import requests, bs4, time, textmyself, webbrowser

def makeBank(url, htmlClass):
    page = requests.get(url)
    page.raise_for_status()
    pageSoup = bs4.BeautifulSoup(page.text, "html.parser")
    elems = pageSoup.select('.' + htmlClass)
    return elems

updated = False
tags = makeBank('http://www.realclearpolitics.com/epolls/2016/president/us/general_election_trump_vs_clinton-5491.html', 'dem')
avg = tags[0].getText()
print('Current matchup is: ' + avg)

while not updated:
    newTags = makeBank('http://www.realclearpolitics.com/epolls/2016/president/us/general_election_trump_vs_clinton-5491.html', 'dem')
    curAvg = newTags[0].getText()
    if avg != curAvg:
        toText = "NEW POLL:\nPrevious H2H matchup was " + avg +"\nNew H2H matchup is " + curAvg
        textmyself.textmyself(toText)
        webbrowser.open('https://www.predictit.org/')
        webbrowser.open('http://www.realclearpolitics.com/epolls/2016/president/us/general_election_trump_vs_clinton-5491.html')
        updated = True
    time.sleep(5)
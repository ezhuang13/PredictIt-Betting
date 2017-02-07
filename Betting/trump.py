#predictit.py
#Monitors the number of POF statements issued by Trump
import textmyself, requests, bs4, time, webbrowser

#accepts URL and class, returns list of Tag objects under that class
def makeBank(url, htmlClass):
    page = requests.get(url)
    page.raise_for_status()
    pageSoup = bs4.BeautifulSoup(page.text, "html.parser")
    elems = pageSoup.select('.' + htmlClass)
    return elems

updated = False
tags = makeBank('http://www.politifact.com/personalities/donald-trump/', 'chartlist__count')
numPOF = tags[5].getText()
numPOF = numPOF[:2]
print('Current number of POF is: ' + numPOF)

while not updated:
    newTags = makeBank('http://www.politifact.com/personalities/donald-trump/', 'chartlist__count')
    newNumPOF = newTags[5].getText()
    newNumPOF = newNumPOF[:2]
    if newNumPOF != numPOF:
        textmyself.textmyself("POF FOUND YO")
        webbrowser.open('https://www.predictit.org/Market/2427/How-many-totally-false-statements-will-Trump-make-in-September')
        webbrowser.open('http://www.politifact.com/personalities/donald-trump/')
        updated = True
    time.sleep(5)
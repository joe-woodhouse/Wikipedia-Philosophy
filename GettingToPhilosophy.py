import requests
from bs4 import BeautifulSoup
import re

urlbase='https://en.wikipedia.org'
target = 'https://en.wikipedia.org/wiki/Philosophy'

BADLINKS = ['Help:', 'File:', 'Wikipedia:', 'Talk:', '_\(disambiguation\)', '/upload.wikimedia', 'redline=1']
BADTAGS = ['i', 'em', 'cite', 'tr', 'sup', 'span', 'small']
BADCLASSES = ['navbox', 'vertical-navbox', 'toc', 'mw-editsection']

c, MAX = 0, 100
history = list()

url = input('Enter URL, or RETURN for random: ')
if len(url) < 1 : url = 'https://en.wikipedia.org/wiki/Special:Random'
r = requests.get(url)
url = r.url  # Get the final URL if redirected

while url != target and c < MAX :
    history.append(url)
    c += 1
    url = None
    soup = BeautifulSoup(r.text, 'html.parser').find(id='mw-content-text')  # Only need main Wiki body
    for tag in soup.find_all(BADTAGS) : tag.replace_with("")
    for tag in soup.find_all(class_=BADCLASSES) : tag.replace_with("")
    paras = soup.find_all(["p", "li"])
    for p in paras :
        # Strip parentheses without breaking links that contain them
        p = str(p)
        while re.search("[^_]\(", p) : p = re.sub("[^_]\(.*?\)", "", p)
        found = None
        for link in BeautifulSoup(p, "html.parser").select("a") :
            href = link.get('href')
            if re.search('|'.join(BADLINKS), href) :
                continue  # check next link
            else :
                r = requests.get(urlbase + href)
                url = r.url  # final URL if redirected
                print (url)
                if url in history :
                    print ('Loop detected, halting')
                    quit()
                found = True
                break  # no more links needed
            # Keep checking links in the current para
        if found :
            break  # no more paras needed
        # Keep checking a new para for links
    if not url :
        print ('No valid links, halting')
        quit()
    # Reaching this point means we have a valid link

if c == MAX :
    print ('Reached', MAX, 'links, halting')
else :
    print ('Reached target in', c, 'steps')

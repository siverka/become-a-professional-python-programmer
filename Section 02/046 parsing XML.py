from bs4 import BeautifulSoup
import urllib.request

req = urllib.request.urlopen('http://feeds.bbci.co.uk/news/video_and_audio/science_and_environment/rss.xml')
print(req.status)

xml = BeautifulSoup(req, 'xml')

# Find all in "link" tags
# Go to every lnk and check response status
for item in xml.findAll('link'):
    url = item.text
    news = urllib.request.urlopen(url).read()

    page = BeautifulSoup(news)
    for p in page.findAll('p'):
        print(p.text)

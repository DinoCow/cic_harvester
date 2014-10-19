from bs4 import BeautifulSoup
import urllib2

response = urllib2.urlopen('http://www.cic.gc.ca/english/information/applications/guides/EG7TOC.asp')
html = response.read()
soup = BeautifulSoup(html)

print(soup.get_text())



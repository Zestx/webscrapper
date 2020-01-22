from bs4 import BeautifulSoup
import urllib.request

#targeted url
url='https://www.yelp.com/biz/milk-and-cream-cereal-bar-new-york?osq=Ice+Cream'

#open the url
targetURL=urllib.request.urlopen(url)

#parse the page in a bs object
soup=BeautifulSoup(targetURL, 'html.parser')

print(soup.pretiffy())

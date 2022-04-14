import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
 
class Inspector:
  def __init__(self,URL):
    self.base = URL
    self.urls = [URL]
  def scan(self,url = None):
    if not url:
      url = self.base
    res = requests.get(url)
    soup = BeautifulSoup(res.text,"html.parser")
    links = soup.find_all("a")
    for link in links:
      link = link.get("href")
      link = urljoin(self.base,link);
      if self.base in link and link not in self.urls:
        print(link)
        self.urls.append(link)
        self.scan(link)
  
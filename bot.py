import requests
import sched, time
from bs4 import BeautifulSoup

URL = "https://laane.barbora.ee/toode/kohvioad-kronung-jacobs-1-kg"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

initialPrice = soup.find("span", class_="b-product-price-current-number")['content']

print(initialPrice)

s = sched.scheduler(time.time, time.sleep)
def priceChecker(sc): 
    print("Checking price..")
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    currentPrice = soup.find("span", class_="b-product-price-current-number")['content']
    if (currentPrice != initialPrice):
        if(currentPrice<initialPrice):
            print("Hind on langenud")

    s.enter(300, 1, priceChecker, (sc,))

s.enter(300, 1, priceChecker, (s,))
s.run()
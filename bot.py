import requests
import sched, time
from bs4 import BeautifulSoup

while True:
    try:
        desiredPrice = float(input("Sisestage soovitud hind: "))
        print(desiredPrice)
        break
    except:
        print("Peab olema number")

URL = "https://laane.barbora.ee/toode/kohvioad-kronung-jacobs-1-kg"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

initialPrice = soup.find("span", class_="b-product-price-current-number")['content']

print(initialPrice)

s = sched.scheduler(time.time, time.sleep)
def priceChecker(sc): 
    print("Kontrollin hinda..")
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    currentPrice = soup.find("span", class_="b-product-price-current-number")['content']
    if (currentPrice != initialPrice):
        if(desiredPrice<=currentPrice):
            print("Osta!")

    s.enter(86400, 1, priceChecker, (sc,))

s.enter(86400, 1, priceChecker, (s,))
s.run()
import requests
import sched, time
import smtplib, ssl
from bs4 import BeautifulSoup

sender_email = "scrapeprojectnotifier@gmail.com"
receiver_email = "kenneth.lember@ametikool.ee"
message = """\
Subject: SkyScrape toote hinna teavitus
a
Teie valitud toote hind on langenud alla soovitud vaartuse, mine osta!

SkyScrape."""
port = 465  # For SSL
password = input("Emaili konto salasõna: ")




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
    print(currentPrice)
    if (1):
        if(int(currentPrice)<=desiredPrice):
            print("Osta!")
            # Create a secure SSL context
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)

    s.enter(60, 1, priceChecker, (sc,))

s.enter(60, 1, priceChecker, (s,))
s.run()
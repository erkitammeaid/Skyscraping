import requests
import sched
import time
import smtplib
import ssl
import mysql.connector
from bs4 import BeautifulSoup

sender_email = "scrapeprojectnotifier@gmail.com"
receiver_email = "erki.tammeaid@ametikool.ee"
message = """\
Subject: SkyScrape toote hinna teavitus

Valitud toote hind on langenud alla soovitud vaartuse, mine osta!

SkyScrape."""
port = 465  # For SSL
password = input("Emaili konto salasõna: ")

mydb = mysql.connector.connect(
    host="d98711.mysql.zonevs.eu",
    user="d98711_scraper",
    password="2021projekt"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")


while True:
    try:
        desiredPrice = float(input("Sisestage soovitud hind: "))
        print(desiredPrice)
        break
    except:
        print("Peab olema number")

URL = "https://laane.barbora.ee/toode/kohviuba-arabica-paulig-1-kg"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

initialPrice = soup.find("span", class_="b-product-price-current-number")['content']

print(initialPrice)

s = sched.scheduler(time.time, time.sleep)

def priceChecker(sc):
    print("Kontrollin hinda..")
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    currentPrice = soup.find(
        "span", class_="b-product-price-current-number")['content']
    print(currentPrice)

    if(float(currentPrice) <= desiredPrice):
        print("Osta!")
        # Create a secure SSL context
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
            
            

    s.enter(600, 1, priceChecker, (sc,))


s.enter(600, 1, priceChecker, (s,))
s.run()

import mysql.connector

mydb = mysql.connector.connect(
    host="d98711.mysql.zonevs.eu",
    user="d98711_scraper",
    password="2021projekt",
    database="skyscraper"
)

print(mydb)

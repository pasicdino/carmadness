from bs4 import BeautifulSoup
import requests
import time


ads = []

for page_number in range(1, 2):
    print(page_number)
    url = 'https://www.marktplaats.nl/l/auto-s/p/' + str(page_number) + '/#f:10898'

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    lists = soup.find_all('li', class_='hz-Listing')
    ran, engine_type, transmission, body = None, None, None, None
    for list in lists:
        title = list.find('h3', class_='hz-Listing-title')
        if title!=None:
            title = title.text
        seller = list.find('span', class_='hz-Listing-seller-name')
        if seller!=None:
            seller = seller.text
        price = list.find('div', class_="hz-Listing-price")
        if price!=None:
            price = price.text[2:]
        location = list.find('div', class_='hz-Listing-sellerLocation')
        if location!=None:
            location = location.text
        year = list.find('span', class_="hz-Attribute")
        if year!=None:
            year = year.text
            ran = list.find('span', class_="hz-Attribute").find_next('span')
            if ran!= None:
                ran = ran.text
                engine_type = list.find('span', class_="hz-Attribute").find_next('span').find_next('span')
                if engine_type!=None:
                    engine_type = engine_type.text
                    transmission = list.find('span', class_="hz-Attribute").find_next('span').find_next('span').find_next('span')
                    if transmission!=None:
                        transmission = transmission.text
                        body = list.find('span', class_="hz-Attribute").find_next('span').find_next('span').find_next('span').find_next('span')
                        if body !=None:
                            body = body.text
        info = [title, seller, price, location, year, ran, engine_type, transmission, body]
        ads.append(info)

import csv
with open('C:/Users/01din/Documents/University/DA/madness/data.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    # write the header row
    writer.writerow(["Title", "Seller", "Price", "Location", "Year", "Ran", "Engine Type", "Transmission", "Body"])

    # write the data rows
    for row in ads:
        writer.writerow(row)
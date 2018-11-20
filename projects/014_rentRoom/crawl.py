# -*- coding: utf-8 -*-
import importlib
import sys
importlib.reload(sys)

from bs4 import BeautifulSoup
import requests
import csv

url = "https://wh.58.com/pinpaigongyu/pn/{page}/?minprice=1000_1500"


page = 0
csv_file = open('rent.csv','w')
csv_writer = csv.writer(csv_file,delimiter=',')

while True:
    page += 1
    print("Fetch:",url.format(page=page))
    response = requests.get(url.format(page=page))
    html = BeautifulSoup(response.text,"lxml")
    # print(html)
    house_list = html.select(".list > li")

    # 循环在读不到新的房源的时候结束
    if not house_list:
        break

    for house in house_list:
        house_title = house.select("h2")[0].string
        house_url = "https://wh.58.com/%s" % (house.select("a")[0]["href"])
        house_info_list = house_title.split()

        if "公寓" in house_info_list[1] or "青年社区" in house_info_list[1]:
            house_location = house_info_list[0]
        else: 
            house_location = house_info_list[1]

        house_money = house.select(".money")[0].select("b")[0].string
        # print(house_title,house_money,house_url)
        # print(house_money.decode("GBK"))
        csv_writer.writerow([house_title.encode("GBK"),house_location.encode('GBK'),house_money.encode('GBK'),house_url.encode("GBK")])

csv_file.close()

import requests
import os
import csv
from bs4 import BeautifulSoup
import driver
import sqlite3
import datetime
import re
import time

n = sqlite3.connect('phone.db')


header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'b=1|00000000355f9f91110204a4756931f6; bha_code=en; _ga=GA1.3.1367231939.1675932711; _gid=GA1.3.613567833.1675932711; PushSubscriberStatus=CLOSED; peclosed=true; ci=Delhi-NCR; ci=Delhi-NCR; tci=Delhi-NCR; JSESSIONID=40D93C933A1B930DB44BE6667C59D3ED; JSESSIONID=40D93C933A1B930DB44BE6667C59D3ED; _gat=1',
    'DNT': '1',
    'Host': 'www.asklaila.com',
    'Referer': 'https://www.asklaila.com/search/Delhi-NCR/-/restaurant/',
    'sec-ch-ua': '"Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.78'
}

#Delhi-NCR
#Bangalore
#Mumbai
#Chennai
#Kolkata
#Hyderabad
#Ahmedabad
#2900

u = "https://www.asklaila.com/search/Ahmedabad/-/ice-cream-shop/"

for k in range(0,10000000,20):
    print(k)
    if not k==0:
        d = requests.get(u+str(k)+'/', headers=header)
    else:
        d = requests.get(u, headers=header)
    data = BeautifulSoup(d.text, 'html.parser')
    x = data.find_all("label", {"class": "phonedisplay"})
    for i in x:
        y = i.text
        s = y.replace('\n', '').replace('\t', '').replace(' ', '')
        z = s.split(',')
        for j in z:
            if j[1] == '9' or j[1] == '8' or j[1] == '7':
                m = j
                print(m)
                n.execute("INSERT INTO indian_mobile_numbers(number,date) VALUES('"+str(m)+"','2023-03-10')")
                n.commit()


import time
import sqlite3
import requests
from bs4 import BeautifulSoup

import threading


url="https://www.2embed.to/library/movie/"

def extract(i):
    try:
        headers = {
            'authority': 'www.2embed.to',
            'method': 'HEAD',
            'path': '/embed/tmdb/movie?id='+str(i),
            'scheme': 'https',
            'accept': '*/*',
            'accept-encodng': 'gzip,deflate,br',
            'accept-language': 'en-US,en;q=0.9',
            'cookie': '_ga=GA1.1.1668231842.1666602675; __atuvc=6%7C43; __atuvs=635656aa412b7cfa005; _ga_8ST3M82VHM=GS1.1.1666602674.1.1.1666603407.0.0.0',
            'referer': 'https://www.2embed.to/embed/tmdb/movie?id='+str(i),
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': "Windows",
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
        }

        x=requests.get(url+str(i),timeout=1).text
        b=BeautifulSoup(x)
        img_url=b.find_all('img')[1]['src']
        name=b.find('h2').text
        murl='https://www.2embed.to/embed/tmdb/movie?id='+str(i)
        genre=''
        db = sqlite3.connect('movies.db')
        for g in b.find_all('div',{'class':'row-line'})[2].text.replace(' ','').split('\n'):
            if not (g=='' or g=='Genres:' or g=='Genre:'):
                genre=genre+g
        tag=''
        for g in b.find_all('div',{'class':'row-line'})[3].text.replace(' ','').split('\n'):
            if not (g=='' or g=='Casts:'):
                tag=tag+g
        tags=name+name.replace('-','').replace(' ','')+tag
        db.execute("INSERT INTO move (name,url,genre,img_url,tags,tmdb_id) VALUES ('" + str(name) + "','" + str(murl) + "','" + str(genre) + "','" + str(img_url) + "','" + str(tags) + "','"+str(i)+"')")
        db.commit()
        db.close()
    except:
        print(i)


for x in range(924511,962232):
    fuc=threading.Thread(target=extract,args=(x,))
    fuc.start()
    if ((x%10)==0):
        fuc.join()
    time.sleep(0.2)

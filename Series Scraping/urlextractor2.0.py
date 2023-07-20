import threading
import sqlite3
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import undetected_chromedriver as uc
PATH = "D:\chromedriver.exe"

browser = uc.Chrome(use_subprocess=True)
# time.sleep(20)

db=sqlite3.connect('noonemovies.db')

start_point=0

f=open('series.txt','r').read().split('\n')



def tabopener(url,season,episode):
    # browser.get('http://fmovies.to')

    # Lets open https://www.bing.com/ in the second tab

    browser.execute_script("window.open('"+url+"/"+str(season)+"-"+str(episode)+"')")

    # browser.switch_to.window("thirdtab")
    # time.sleep(21)
    # Lets open https://www.facebook.com/ in the third tab
    # browser.execute_script("window.open('about:blank','thirdtab');")
    # browser.switch_to.window("thirdtab")
    # browser.get('https://www.facebook.com/')

def tab_clicker(btn_id):
    x=True
    while x:
        try:
            st2 = browser.find_element(By.XPATH, "//div[@data-id='"+str(btn_id)+"']")
            browser.execute_script("arguments[0].click();", st2)
            x=False
        except:
            if (browser.current_url=='https://fmovies.to/') or (browser.current_url=='https://fmovies.to') or (browser.current_url=='fmovies.to'):
                break
            x=True



def loopfunc():
    count = 1
    for i in range(8325):
        url=f[i]
        url="https://fmovies.to"+url
        browser.get(url)
        firsttab=browser.current_window_handle
        if count==1:
            time.sleep(30)
            count+=1
        data=browser.page_source
        b1 = BeautifulSoup(data).find_all("div", {"class": "range"})
        name=BeautifulSoup(data).find('h1',{'itemprop':'name'}).text
        rd=BeautifulSoup(data).find_all('div',{'class':'meta'})[1]
        img_url=BeautifulSoup(data).find_all('img',{'itemprop':'image'})[0]['src']
        print(img_url)
        genre=''
        for gen in rd.find_all('div')[1].find_all('a'):
            genre=genre+gen.text

        date=(rd.find_all('div')[2].find('span',{'itemprop':'dateCreated'}).text).split('-')[0]

        cast=''
        for gen in rd.find_all('div')[5].find_all('a'):
            cast+=gen.text

        name=name+'('+date+')'

        tags=name+','+name.replace(' ','')+','+cast

        seasons=[]
        for b in b1:
            seasons.append(int(b['data-range'].split('-')[1]))
        ss=1
        for season in seasons:
            if 30 in seasons:
                break
            if season>30:
                print("broken")
                break
            for episode in range(1,season+1):
                fuck=threading.Thread(target=tabopener,args=(url,ss,episode))
                fuck.start()
                time.sleep(0.5)

                # if break1:
                #     break1=False
                #     break
            fuck.join()

            fuck = threading.Thread(target=tabopener, args=('https://fmovies.to/series/dark-side-of-comedy-pm6nx', 1, 1))
            fuck.start()
            fuck = threading.Thread(target=tabopener, args=('https://fmovies.to/series/dark-side-of-comedy-pm6nx', 1, 2))
            fuck.start()
            time.sleep(2)
            btnid=[41,28,45,40]

            # print(episodetoken)
            for bt in btnid:
                episodetoken = browser.window_handles
                for episode in episodetoken:
                    try:
                        if episode==firsttab:
                            continue
                        browser.switch_to.window(episode)
                        time.sleep(0.5)
                        tab_clicker(bt)
                    except:
                        pass
                for episode in episodetoken:
                    try:
                        if episode==firsttab:
                            continue
                        browser.switch_to.window(episode)
                        time.sleep(0.5)
                        ep=(browser.current_url).split('-')[-1]
                        x1 = BeautifulSoup(browser.page_source).find('iframe')['src']
                        server=btnid.index(bt)+1
                        # print(ep,x1,server,tags)
                        if not (db.execute("SELECT * FROM series WHERE url='"+x1+"'")==None):
                            if ep=='full':
                                ep='1'
                            db.execute("INSERT INTO series (name,season,episode,server,url,genre,img_url,tags) VALUES ('"+str(name)+"','"+str(ss)+"','"+str(ep)+"','"+str(server)+"','"+str(x1)+"','"+str(genre)+"','"+str(img_url)+"','"+str(tags)+"')")
                            db.commit()
                            print(url,ss,' - ',ep)
                    except:
                        pass




            # fuck.join()
            ss+=1
            browser.execute_script("window.open('https://fmovies.to/')")
            time.sleep(2)
            lasttab =browser.current_window_handle
            episodetoken = browser.window_handles
            for episode in episodetoken:
                if episode==lasttab:
                    continue
                browser.switch_to.window(episode)
                browser.close()
            browser.switch_to.window(lasttab)



loopfunc()


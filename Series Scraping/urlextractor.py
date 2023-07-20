from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import undetected_chromedriver as uc
PATH = "D:\chromedriver.exe"
browser = uc.Chrome(use_subprocess=True)
browser1 = uc.Chrome(use_subprocess=True)
browser2 = uc.Chrome(use_subprocess=True)
browser3 = uc.Chrome(use_subprocess=True)
count=0
for season in range(1,100):
    for episode in range(1,100):
        turl="https://fmovies.to/series/the-damelio-show-j2824/"+str(season)+"-"+str(episode)
        browser.get("https://fmovies.to/series/the-damelio-show-j2824/"+str(season)+"-"+str(episode))
        st1 = browser.find_element(By.XPATH, "//div[@data-id='41']")
        browser.execute_script("arguments[0].click();", st1)
        time.sleep(1.5)
        if not (browser.current_url==turl):
            print("season "+str(season)+" complete")
            count+=1
            break
        else:
            count=0
        x1=browser.page_source
        st2=browser.find_element(By.XPATH,"//div[@data-id='28']")
        browser.execute_script("arguments[0].click();", st2)
        time.sleep(1.5)
        x2 = browser.page_source
        st2 = browser.find_element(By.XPATH, "//div[@data-id='45']")
        browser.execute_script("arguments[0].click();", st2)
        time.sleep(1.5)
        x3 = browser.page_source
        st2 = browser.find_element(By.XPATH, "//div[@data-id='40']")
        browser.execute_script("arguments[0].click();", st2)
        time.sleep(1.5)
        x4 = browser.page_source
        b1=BeautifulSoup(x1).find('iframe')['src']
        b2=BeautifulSoup(x2).find('iframe')['src']
        b3=BeautifulSoup(x3).find('iframe')['src']
        b4=BeautifulSoup(x4).find('iframe')['src']

        print("episode "+str(episode)+" - ",b1,b2,b3,b4)
        print()
        print()

    if (count==2):
        print("series complete")
        count=0
        break
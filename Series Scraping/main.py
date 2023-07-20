import time
import undetected_chromedriver as uc
PATH = "D:\chromedriver.exe"
browser = uc.Chrome(use_subprocess=True)
file1 = open('series.txt', 'r')
Lines = (file1.read()).split('\n')

for i in Lines:
    file2 = open('series2.txt', 'a')
    browser.get("https://web.fmovies.to"+i)
    time.sleep(0.5)
    print(browser.current_url)
    file2.writelines(str(browser.current_url))

    file2.close()

browser.close()




# # c = browser.find('div',{'class': 'episode'})
# # content = c.find_all('a')
# # print(content)
# st=browser.find_element(By.XPATH,"//div[@data-id='41']")
# browser.execute_script("arguments[0].click();", st)
# time.sleep(0.5)
# print(browser.page_source)
#
# # PATH = "D:\chromedriver.exe"
# # driver = webdriver.Chrome(PATH)
# # driver.get("https://fmovies.to/")
# #time.sleep(1000)

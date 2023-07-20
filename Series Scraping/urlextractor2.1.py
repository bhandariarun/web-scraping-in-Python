from selenium.webdriver import Firefox
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

profile_path = r'D:\geckodriver.exe'
options=Options()
options.set_preference('profile', profile_path)
options.set_preference('network.proxy.type', 1)
options.set_preference('network.proxy.socks', '139.99.237.62')
options.set_preference('network.proxy.socks_port', 80)
options.set_preference('network.proxy.socks_remote_dns', True)
service = Service('D:\\geckodriver.exe')
driver = Firefox(service=service, options=options)
driver.get("https://fmovies.to")
time.sleep(60)
driver.quit()
import time
from selenium import webdriver
from bs4 import BeautifulSoup

keyword = input('Enter a keyword: ')
url = 'https://www.google.com.tw/search?q='+keyword
browser = webdriver.Chrome()
browser.get(url)


while True:
    browser.find_element_by_link_text('下一頁').click()
    
    time.sleep(1)
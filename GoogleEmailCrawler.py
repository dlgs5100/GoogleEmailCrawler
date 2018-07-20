import time
from selenium import webdriver
from bs4 import BeautifulSoup

keyword = input('Enter a keyword:')
page = input('Search page amount:')
url = 'https://www.google.com.tw/search?q='+keyword
browser = webdriver.Chrome()
browser.get(url)


for i in range(1, int(page)):
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    Emails = soup.select('span.st')
    for i in Emails:
       for j in i.text.split(' '):
           if j.find('@mail.taipei.gov.tw.') != -1:
               print(j)
    try:
        browser.find_element_by_link_text('下一頁').click()
    except Exception as msg:
        break

    time.sleep(0.1)

browser.close()
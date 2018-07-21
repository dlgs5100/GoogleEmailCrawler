import time
from selenium import webdriver
from bs4 import BeautifulSoup

def crawl():
    keyword = input('Enter a keyword:')
    page = input('Search page amount:')
    url = 'https://www.google.com.tw/search?q='+keyword
    browser = webdriver.Chrome()
    browser.get(url)


    for i in range(0, int(page)):
        soup = BeautifulSoup(browser.page_source, 'html.parser')

        #print(soup.prettify())

        Emails = soup.select('span.st')
        for i in Emails:
            for j in i.text.split(' '):
                result = findEmail(j,keyword)
                if result != 0:
                    print(result)

        try:
            browser.find_element_by_link_text('下一頁').click()
        except Exception as msg:
            break

        time.sleep(0.1)

    browser.close()

def findEmail(string, mailType):
    t = 0
    startPoint = 0
    endPoint = 0
    atPoint = string.find('@')
    if string.find(mailType) != -1:
        for i in range(atPoint-1, 0, -1):
            if ((ord(string[i])>=48 and ord(string[i])<=57) or 
            (ord(string[i])>=65 and ord(string[i])<=90) or 
            (ord(string[i])>=97 and ord(string[i])<=122) or 
            ord(string[i]) == 45 or ord(string[i]) == 46 or ord(string[i]) == 95):
                t=t+1
            else:
                startPoint = i+1
                break
        for i in range(atPoint, len(string)+1):
            if string[atPoint:i].find('tw') != -1:
                endPoint = i
                break
        return string[startPoint:endPoint]
    else:
        return 0

def main():
    crawl()

if __name__ == "__main__":
    main()
from selenium import webdriver
from selenium.webdriver import ChromeOptions
import time

def get_table(i):
    for j in range(i + 1, len(url)):
        time.sleep(1)
        browser.get(f'{url[j]}')

        div = browser.find_elements_by_class_name('content')
        pan = div[0].find_elements_by_id('pan')
        a = pan[0].find_elements_by_css_selector('a')
        f.write(f'{j + 1} ')
        f.write(a[3].text)
        f.write('\n\n')

        try:
            div = browser.find_elements_by_class_name('detail-content-table')
            td = div[1].find_element_by_css_selector('td')
            f.write(td.text)
            f.write('\n\n') 

        except IndexError:
            td = div[0].find_elements_by_css_selector('td')
            f.write(td[0].text)
            f.write('\n\n')
                
            return get_table(j)
    
    f.close()
    return 0
    

options = ChromeOptions()
options.headless = True


num = 1
browser = webdriver.Chrome()
url = []


for num in range(15):
    time.sleep(1)
    browser.get(f'https://www.green-japan.com/search_key/01?key=jr8w4uiffy2sdol4dg1b&keyword=&page={num + 1}')
    
    if num == 14:
            for j in range(8):
                div = browser.find_elements_by_css_selector('.card-info__wrapper')
                a = div[j].find_element_by_css_selector('a')
                url.append(a.get_attribute('href'))
    
    else:
        for i in range(10):
            div = browser.find_elements_by_css_selector('.card-info__wrapper')
            a = div[i].find_element_by_css_selector('a')
            url.append(a.get_attribute('href'))

print(url[147])
print(len(url))

f = open('/Users/wago55/Desktop/content.txt', 'w')


for i in range(len(url)):
    time.sleep(1)
    browser.get(f'{url[i]}')

    div = browser.find_elements_by_class_name('content')
    pan = div[0].find_elements_by_id('pan')
    a = pan[0].find_elements_by_css_selector('a')
    f.write(f'{i + 1} ')
    f.write(a[3].text)
    f.write('\n\n')
    
    try:
        div = browser.find_elements_by_class_name('detail-content-table')
        td = div[1].find_element_by_css_selector('td')
        f.write(td.text)
        f.write('\n\n') 

    except IndexError:
        td = div[0].find_elements_by_css_selector('td')
        f.write(td[0].text)
        f.write('\n\n')
        
        get_table(i)





    

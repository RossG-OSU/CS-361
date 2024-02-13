#scrape?

import time
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


today = str(date.today())
options = webdriver.FirefoxOptions()
options.add_argument('--headless')
driver = webdriver.Firefox(options=options)

driver.get('https://www.sierraavalanchecenter.org/forecasts/#/central-sierra-nevada')
time.sleep(5)

danger = driver.find_elements(By.CLASS_NAME, 'nac-dangerLabel')
df = open('dangerfile.txt', 'a')
df.write('Avvy Report for ' + today + '\n')

danger = danger[6:9]
for d in danger:
    df.write(d.text + '\n')

titl = []
titles = driver.find_elements(By.TAG_NAME, 'h3')
for t in titles:
    if t.text[0:7] == 'PROBLEM':
        titl.append(t.text)


problems = driver.find_elements(By.CLASS_NAME, 'nac-tinymce')
probs = []
for p in problems:
    if p.text != '':
        probs.append(p.text)

df.write('The Bottom Line: ' + probs[0] + '\n')
i = 1
for t in titl:
    df.write(titl[i-1] + ' '+ probs[i] + '\n')
    i += 1


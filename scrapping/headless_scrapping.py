from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime
import os
import sys

# application_path = os.path.dirname(sys.executable)

now = datetime.now()

month_day_year = now.strftime("%m%d%Y")  # MMDDYYYY

website = "https://www.thesun.co.uk/sport/football/"
path = "C:\\Users\\CASH\\Downloads\\chromedriver"

# headless mode
options = Options()
options.headless = True
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)

driver.get(website)

containers = driver.find_elements(
    by="xpath", value='//div[@class="teaser__copy-container"]')

titles = []
subtitles = []
links = []

for container in containers:
    title = container.find_element(by='xpath', value='./a/h2').text
    subtitle = container.find_element(by='xpath', value='./a/p').text
    link = container.find_element(
        by='xpath', value='./a').get_attribute("href")
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

my_dict = {'title': titles, 'subtitle': subtitles, 'link': links}
df_headlines = pd.DataFrame(my_dict)

file_name = f'headless-{month_day_year}.csv'

# final_name = os.path.join(application_path, file_name)

df_headlines.to_csv(file_name)

driver.quit()

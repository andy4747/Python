from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import pandas as pd

PATH="chromedriver.exe"

#choosing chrome as the browser and passing the path to driver
driver=webdriver.Chrome(PATH)


driver.get("https://youtube.com/feed/trending")


videos=driver.find_elements_by_xpath('//*[@id="video-title"]')
links=[]
for i in videos:
    links.append(i.get_attribute('href'))
total_vids_done=0

#making pandas dataframe colums for link,title and description
df=pd.DataFrame(columns=['link','title','description'])
sleep(10)
for i in links:
    driver.get(i)
    vid_id=i
    vid_title = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR,"h1.title yt-formatted-string"))).text
    vid_description = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div#description yt-formatted-string"))).text
    df.loc[len(df)]=[vid_id,vid_title,vid_description]
    total_vids_done+=1
    print(total_vids_done)
    sleep(3)

df.to_csv("scraped_yt_vids.csv", encoding='utf-8', index=False)

sleep(5)

driver.quit()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# options.add_argument('--headless')#usar modo inv
options.add_argument('--start-maximized')
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)


driver.get('https://www.youtube.com/results?search_query=python')

videos = driver.find_elements(By.ID, 'thumbnail')

for i in range(20):
    qtdScroll = i * 1000
    driver.execute_script(f'window.scroll(0, {qtdScroll})')
    time.sleep(2)
for video in videos:
    print(video.get_attribute('href'))

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

# initialize channel_id, youtube url, and list of video ids
channel_id = "@t3dotgg"
url = f"https://www.youtube.com/{channel_id}/videos"
video_ids = []

# initialize headless firefox
options = Options()
options.add_argument("-headless")
driver = webdriver.Firefox(
    options=options, service=Service(executable_path=GeckoDriverManager().install())
)
# go to URL
driver.get(url)
time.sleep(5)

# get document height for scrolling
height = driver.execute_script("return document.documentElement.scrollHeight")
lastheight = 0

# continue   until end of page
while True:
    if lastheight == height:
        break
    lastheight = height
    driver.execute_script("window.scrollTo(0, " + str(height) + ");")
    time.sleep(2)
    height = driver.execute_script("return document.documentElement.scrollHeight")

# find all elements with id video-title-link, get their href, and store in video_ids array
user_data = driver.find_elements(by=By.XPATH, value='//*[@id="video-title-link"]')
for i in user_data:
    link = i.get_attribute("href")
    if not (link is None):
        video_ids.append(link.split("https://www.youtube.com/watch?v=")[1])

# quit driver
driver.quit()

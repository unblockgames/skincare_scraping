from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# This is a script for getting the urls of the brand pages at sephora.
# This should be run first

# Setting up the webdriver with a user agent and attempting to diable pop-ups
opts = Options()
opts.add_argument(
    "user-agent=['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36']")
opts.add_argument("--disable-notifications")
driver = webdriver.Chrome(
    "./sephora_analysis/selenium_scrape/chromedriver", options=opts)

# start at the page listing brands
start_url = "https://sephora.com/brands-list"
driver.get(start_url)

# getting the urls by their xpath //div[2]/ul/li/a
brands = driver.find_elements_by_xpath('//div//ul/li/a')
brands = [a.get_attribute('href')+'/all' for a in brands]

# saving the urls to a text file
with open('sephora_brand_pages.txt', 'w') as f:
    for url in brands:
        f.write(url+'\n')

driver.close()

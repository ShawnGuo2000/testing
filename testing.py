from selenium import webdriver
from selenium.webdriver.chrome.options import Options

"""chrome_options = Options()
chrome_options.add_argument("--headless")"""

driver = webdriver.Chrome("D:/project/chromedriver/chromedriver.exe")
driver.get('https://www.google.com/')
driver.find_element_by_name('q').send_keys('software testing')
driver.find_element_by_name('q').send_keys(u'\ue007')
print(driver.title)
driver.close()
driver.quit()
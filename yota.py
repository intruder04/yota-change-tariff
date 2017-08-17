import time
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
i = 0
j = 0

arg = ""

for eachArg in sys.argv:
    arg = eachArg

if len(sys.argv) < 2:
    print("no args. use on or off!!")
    exit()

chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get('https://my.yota.ru')
time.sleep(1)
search_box = driver.find_element_by_name('IDToken1')
search_box.send_keys('nomer')
time.sleep(1)
search_box2 = driver.find_element_by_xpath(
    '//input[contains(@type, "password")]')
search_box2.send_keys('parol')
time.sleep(1)

button = driver.find_element_by_id('doSubmitLoginForm')
button.click()
time.sleep(4)

if arg == "on":
    increase_button = driver.find_element_by_class_name('increase')
    while i < 14:
        i = i + 1
        increase_button.click()
if arg == "off":
    decrease_button = driver.find_element_by_class_name('decrease')
    while j < 11:
        j = j + 1
        decrease_button.click()

time.sleep(1)

submit_button = driver.find_element_by_xpath("//a[contains(.,'Подключить')]")
submit_button.click()

time.sleep(2)
driver.quit()
exit()

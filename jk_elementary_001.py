from selenium import webdriver
from time import sleep
import pandas as pd

USER = "*******"
PASS = "*******"

print("Here")

# GoogleCromeを起動
browser = webdriver.Chrome(r"C:\Users\yosak\Desktop\JKMYPython\chromedriver.exe")
browser.implicitly_wait(3)

sleep(3)


# ログインするサイトにアクセス
url_login = "https://www.xxxxxxxxxx.com/"
browser.get(url_login)
sleep(1)

# テキストボックス入力
elem = browser.find_element_by_id("staff_code")
elem.clear()
elem.send_keys(USER)
elem = browser.find_element_by_id("staff_password")
elem.clear()
elem.send_keys(PASS)

sleep(1)

elem_login_btn = browser.find_element_by_class_name("btnArea03")
elem_login_btn.click()

sleep(3)

elem_search_btn = browser.find_element_by_class_name("search")
elem_search_btn.click()

sleep(3)

browser.quit()

# フォームを送信
print("Good")

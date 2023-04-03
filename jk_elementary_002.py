from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

USER = "*******"
PASS = "*******"

print("Here Here")

browser = webdriver.Chrome(r"C:\Users\yosak\Desktop\JKMYPython\chromedriver.exe")
browser.implicitly_wait(3)

sleep(3)

# ログインするサイトにアクセス
url_login = "https://www.xxxxxxxxxx.com/"
browser.get(url_login)

sleep(1)

elem_username = browser.find_element_by_id("staff_code")
elem_username.send_keys(USER)

elem_userpass = browser.find_element_by_id("staff_password")
elem_userpass.send_keys(PASS)

sleep(1)

elem_login_btn = browser.find_element_by_class_name("btnArea03")
elem_login_btn.click()

sleep(3)

browser.quit()
print("Good")

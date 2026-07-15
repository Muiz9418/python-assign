"""
Day 37 - Selenium Basics: Cookie Clicker Bot
Uses Selenium WebDriver to automatically play the Cookie Clicker
game: click the cookie repeatedly and buy upgrades with earnings.
Requires: pip install selenium, and a matching chromedriver.
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.maximize_window()

# Accept the cookie consent / choose language, then click the big cookie
time.sleep(2)
cookie = driver.find_element(By.ID, "bigCookie")

for _ in range(200):
    cookie.click()

# Buy the cheapest available upgrade repeatedly
for i in range(1, 6):
    try:
        item = driver.find_element(By.ID, f"product{i}")
        item.click()
    except Exception:
        continue

money_display = driver.find_element(By.ID, "money").text
print(f"Current cookies: {money_display}")

driver.quit()

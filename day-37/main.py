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

# Wait for page to fully load
time.sleep(5)

# Click the English language button to dismiss language selector
try:
    # Try to find and click the English language button
    eng_button = driver.find_element(By.XPATH, "//a[@onclick=\"Game.SetLanguage('EN');\"]")
    eng_button.click()
    print("Clicked English language selector")
    time.sleep(3)
except Exception:
    # If we can't click it, just proceed - we'll remove the overlay with JavaScript
    pass

# Wait for the game to finish loading
time.sleep(3)

# Remove or hide the darken overlay that blocks clicks (language selection popup)
driver.execute_script("document.getElementById('darken').style.display='none';")
print("Removed language selection overlay")

# Get the big cookie element
cookie = driver.find_element(By.ID, "bigCookie")
print("Found the big cookie!")

for _ in range(200):
    cookie.click()

# Buy the cheapest available upgrade repeatedly
for i in range(1, 6):
    try:
        item = driver.find_element(By.ID, f"product{i}")
        item.click()
    except Exception:
        continue

# Get cookie count - try different possible selectors
try:
    money_display = driver.find_element(By.ID, "cookies").text
    print(f"Current cookies: {money_display}")
except Exception:
    try:
        money_display = driver.find_element(By.CSS_SELECTOR, "#cookies .title").text
        print(f"Current cookies: {money_display}")
    except Exception as e:
        print(f"Could not find cookie count display: {e}")

driver.quit()

"""
Day 38 - Internet Speed Twitter Bot
Runs an internet speed test on speedtest.net via Selenium, extracts
the download/upload speed, and posts a complaint tweet to your ISP
if the speed is below what you're paying for.
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

PROMISED_DOWN = 100  # Mbps promised by your ISP
PROMISED_UP = 20

driver = webdriver.Chrome()
driver.get("https://www.speedtest.net/")

go_button = driver.find_element(By.CLASS_NAME, "start-text")
go_button.click()

time.sleep(60)  # allow the test to finish

download_speed = driver.find_element(By.CLASS_NAME, "download-speed").text
upload_speed = driver.find_element(By.CLASS_NAME, "upload-speed").text

driver.quit()

print(f"Download: {download_speed}Mbps, Upload: {upload_speed}Mbps")

if float(download_speed) < PROMISED_DOWN or float(upload_speed) < PROMISED_UP:
    # In the real project this section logs into Twitter with Selenium
    # and tweets a complaint tagging the ISP's support handle.
    tweet_text = (
        f"Hey Internet Provider, why is my internet speed "
        f"{download_speed}down/{upload_speed}up when I pay for "
        f"{PROMISED_DOWN}down/{PROMISED_UP}up?"
    )
    print("Would tweet:", tweet_text)

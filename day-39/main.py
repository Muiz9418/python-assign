"""
Day 39 - LinkedIn Auto Job Application Bot
Logs into LinkedIn, searches for jobs matching a keyword, and
auto-applies to postings that have an "Easy Apply" button.
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

EMAIL = "your_email@example.com"
PASSWORD = "your_password"
JOB_TITLE = "Python Developer"
LOCATION = "Remote"

driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/login")

driver.find_element(By.ID, "username").send_keys(EMAIL)
driver.find_element(By.ID, "password").send_keys(PASSWORD, Keys.ENTER)
time.sleep(3)

search_url = (
    f"https://www.linkedin.com/jobs/search/?keywords={JOB_TITLE.replace(' ', '%20')}"
    f"&location={LOCATION}&f_AL=true"  # f_AL=true filters to Easy Apply jobs
)
driver.get(search_url)
time.sleep(3)

job_cards = driver.find_elements(By.CLASS_NAME, "job-card-container")

for job in job_cards[:10]:
    job.click()
    time.sleep(2)
    try:
        easy_apply_button = driver.find_element(By.XPATH, "//button[contains(., 'Easy Apply')]")
        easy_apply_button.click()
        time.sleep(2)
        # A real bot would step through the multi-page application form here,
        # filling fields and clicking "Next" / "Submit application".
        submit_button = driver.find_element(By.XPATH, "//button[contains(., 'Submit application')]")
        submit_button.click()
        print("Applied to a job.")
    except Exception:
        print("No Easy Apply available for this listing, skipping.")

driver.quit()

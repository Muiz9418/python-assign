"""
Day 46 - Automated Cover Letter Generator
Scrapes a job listing's title/company from a job board, then fills
those details into a cover letter template.
"""
import requests
from bs4 import BeautifulSoup

JOB_URL = "https://example-job-board.com/jobs/12345"  # replace with a real listing

response = requests.get(JOB_URL)
soup = BeautifulSoup(response.text, "html.parser")

# Selectors will vary by site; inspect the page to find the right tags
job_title = soup.find("h1").get_text().strip() if soup.find("h1") else "the position"
company_name = soup.find(class_="company-name")
company_name = company_name.get_text().strip() if company_name else "your company"

with open("cover_letter_template.txt") as file:
    letter = file.read()

letter = letter.replace("[JOB_TITLE]", job_title)
letter = letter.replace("[COMPANY_NAME]", company_name)
letter = letter.replace("[YOUR_NAME]", "Your Name")

with open("cover_letter.txt", "w") as file:
    file.write(letter)

print(letter)

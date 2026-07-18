"""
Day 46 - Automated Cover Letter Generator
Scrapes a job listing's title/company from a job board, then fills
those details into a cover letter template.
"""
import requests
from bs4 import BeautifulSoup
import os
import sys

# Replace with a real job listing URL
# Example: "https://www.python.org/jobs/XXXX/"
JOB_URL = "https://www.python.org/jobs/8105/"  # Computational Photonics Engineer

# Path to template file
TEMPLATE_PATH = "day-46/cover_letter_template.txt"
OUTPUT_PATH = "day-46/cover_letter.txt"

# Check if template exists
if not os.path.exists(TEMPLATE_PATH):
    print(f"Error: Template file not found at {TEMPLATE_PATH}")
    print("Creating a sample template file...")

    sample_template = """Dear Hiring Manager at [COMPANY_NAME],

I am writing to express my strong interest in the [JOB_TITLE] position at [COMPANY_NAME].

With my background and skills, I believe I would be an excellent fit for this role. I am excited about the opportunity to contribute to your team and help [COMPANY_NAME] achieve its goals.

Thank you for considering my application. I look forward to discussing how I can contribute to [COMPANY_NAME].

Sincerely,
[YOUR_NAME]"""

    with open(TEMPLATE_PATH, "w") as f:
        f.write(sample_template)
    print(f"Sample template created at {TEMPLATE_PATH}")

try:
    # Fetch the job listing
    print(f"Fetching job listing from: {JOB_URL}")
    response = requests.get(JOB_URL, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # For python.org job board:
    # The job listing section contains divs with breadcrumbs-job class
    # Inside is an h1 with the job title and company

    job_title = "the position"
    company_name = "your company"

    # Look for all h1 tags and find the one with job info (contains multiple text nodes)
    for h1 in soup.find_all("h1"):
        text_lines = [line.strip() for line in h1.stripped_strings]
        # Filter out "New" and empty lines
        text_lines = [line for line in text_lines if line and line.lower() != "new"]

        # The job listing h1 will have at least 2 lines (title and company)
        if len(text_lines) >= 2 and "jobs on" not in text_lines[0].lower():
            job_title = text_lines[0]
            company_name = text_lines[1]
            break

    # If we didn't find it that way, try looking in the "Job Title" section
    if job_title == "the position":
        for heading in soup.find_all("h2"):
            if "Job Title" in heading.get_text():
                next_elem = heading.find_next_sibling()
                if next_elem:
                    job_title = next_elem.get_text().strip()
                    break

    # Try to find company in "About the Company" section if not found
    if company_name == "your company":
        for heading in soup.find_all("h2"):
            if "About the Company" in heading.get_text():
                next_elem = heading.find_next_sibling()
                if next_elem:
                    text = next_elem.get_text().strip()
                    # Extract company name (usually first word or first line before "is a")
                    if " is a " in text or " is an " in text:
                        company_name = text.split(" is a ")[0].split(" is an ")[0].strip()
                    else:
                        # Take first significant word
                        first_line = text.split('\n')[0].strip()
                        company_name = first_line.split()[0] if first_line else "your company"
                    break

    print(f"Job Title: {job_title}")
    print(f"Company: {company_name}")

    # Read template
    with open(TEMPLATE_PATH) as file:
        letter = file.read()

    # Replace placeholders
    letter = letter.replace("[JOB_TITLE]", job_title)
    letter = letter.replace("[COMPANY_NAME]", company_name)
    letter = letter.replace("[YOUR_NAME]", "Your Name")  # Replace with your actual name

    # Save the cover letter
    with open(OUTPUT_PATH, "w") as file:
        file.write(letter)

    print(f"\nCover letter generated successfully at {OUTPUT_PATH}")
    print("\n" + "=" * 60)
    print("GENERATED COVER LETTER:")
    print("=" * 60)
    print(letter)

except requests.exceptions.RequestException as e:
    print(f"Error fetching job listing: {e}")
    print("\nPlease ensure:")
    print("1. You have an active internet connection")
    print("2. The JOB_URL is valid and accessible")
    print("3. The website allows scraping")
    sys.exit(1)
except FileNotFoundError as e:
    print(f"Error: Template file not found - {e}")
    sys.exit(1)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    sys.exit(1)

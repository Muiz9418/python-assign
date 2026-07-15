"""
Day 34 - Habit Tracking Project (Pixela API)
Creates a graph on Pixela to track a habit (e.g. exercise minutes)
and posts today's data to it.
"""
import requests
from datetime import datetime

USERNAME = "your_pixela_username"
TOKEN = "your_pixela_token"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
update_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

headers = {"X-USER-TOKEN": TOKEN}

# ---- 1. Create a user ----
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

# ---- 2. Create a graph ----
graph_config = {
    "id": GRAPH_ID,
    "name": "Exercise Graph",
    "unit": "minutes",
    "type": "int",
    "color": "ajisai",  # purple
}
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

# ---- 3. Post today's pixel (habit data) ----
today = datetime.now().strftime("%Y%m%d")
pixel_data = {
    "date": today,
    "quantity": "60",
}
response = requests.post(url=update_endpoint, json=pixel_data, headers=headers)
print(response.text)

# ---- 4. Update an existing pixel ----
update_data = {"quantity": "75"}
response = requests.put(url=f"{update_endpoint}/{today}", json=update_data, headers=headers)
print(response.text)

# ---- 5. Delete a pixel ----
response = requests.delete(url=f"{update_endpoint}/{today}", headers=headers)
print(response.text)

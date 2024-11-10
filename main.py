import requests
from datetime import datetime

# Replace with your Pixela username and token
USERNAME = "your_username"
TOKEN = "your_token"
GRAPH_ID = "your_graph_id"  # Unique identifier for the graph

# Endpoint to create a new Pixela user
pixela_endpoint = "https://pixe.la/v1/users"

# User account parameters for Pixela
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Uncomment this section to create a new user on Pixela
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Endpoint to create a new graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# Graph configuration parameters for Pixela
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",  # Name of the graph
    "unit": "km",             # Unit of measurement for the graph
    "type": "float",          # Data type for entries in the graph
    "color": "ajisai"         # Color of the graph (choose from Pixela's colors)
}

# Headers including token for authentication
headers = {
    "X-USER-TOKEN": TOKEN
}

# Uncomment this section to create the graph on Pixela
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Endpoint to create a pixel (daily entry) in the graph
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# Get today's date in the required format (YYYYMMDD)
today = datetime.now().strftime("%Y%m%d")

# Data for the pixel entry
pixel_data = {
    "date": today,
    "quantity": input("How many kilometers did you cycle today? "),  # User input for today's distance
}

# Send a POST request to add a pixel (entry) to the graph
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

# Endpoint to update the pixel for today's date
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

# New data to update the pixel entry
new_pixel_data = {
    "quantity": "4.5"  # New quantity for the update
}

# Uncomment this section to update today's pixel entry
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

# Endpoint to delete the pixel for today's date
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

# Uncomment this section to delete today's pixel entry
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)

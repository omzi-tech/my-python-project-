import requests

# Define the URL you want to scrape
url = 'https://mytimes.taylors.edu.my/my/'

# Define some dummy cookies
cookies = {
    'cookie1': 'value1',
    'cookie2': 'value2',
    'cookie3': 'value3'
}

# Make the GET request with cookies
response = requests.get(url, cookies=cookies)

print(response)

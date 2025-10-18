import requests

def get_bulk_data():
    # Define the API endpoint URL
    url = 'https://api.scryfall.com/bulk-data'

    try:
        # Make a GET request to the API endpoint using requests.get()
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            posts = response.json()
            return posts
        else:
            print('Error:', response.status_code)
            return None
    except requests.exceptions.RequestException as e: 
        # Handle any network-related errors or exceptions
        print('Error:', e)
        return None
    
def download_api_data(download_uri):
    try:
        response = requests.get(download_uri)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print('Error:', response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None
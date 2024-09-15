import requests
import time

# Configuration
auth_url = 'https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token'  # Replace with the actual URL to get the access key
client_id = 'sh-a4cc91d4-f201-47ff-b14b-f540f88cb8e4'  # Replace with your actual client ID
client_secret = 'dJEvwUiQNGzpJxwt3BDb283eTI9a8TMp'  # Replace with your actual client secret
refresh_interval = 600  # 10 minutes in seconds


def get_new_access_key():
    response = requests.post(auth_url, data={
        'client_id': client_id,
        'client_secret': client_secret
    })

    if response.status_code == 200:
        access_key = response.json().get('access_key')  # Adjust based on the actual JSON response structure
        if access_key:
            print(f"New access key obtained: {access_key}")
            return access_key
        else:
            print("Error: No access key found in the response.")
            return None
    else:
        print(f"Error: Unable to get access key. Status code: {response.status_code}")
        return None


def main():
    access_key = get_new_access_key()
    if access_key is None:
        print("Failed to obtain initial access key. Exiting.")
        return

    while True:
        time.sleep(refresh_interval)  # Wait for the specified interval before refreshing the access key
        access_key = get_new_access_key()
        if access_key is None:
            print("Failed to refresh access key. Exiting.")
            break


if __name__ == "__main__":
    main()

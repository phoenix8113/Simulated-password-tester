import subprocess
import json

def check_default_password(device_ip):
    """
    Check if the default password is still in use for a given IP address.
    """
    default_passwords = ["admin", "password", "1234", "admin123", "default"]
    api_endpoint = f"http://{device_ip}/check_password"

    try:
        # Simulate a request to the API to check the password
        response_json = subprocess.check_output(['curl', '-s', api_endpoint]).decode('utf-8').strip()
        response_data = json.loads(response_json)

        # Assuming the JSON response has a "password" field
        device_password = response_data.get("password", "").lower()

        if device_password in default_passwords:
            print(f"Warning: Default password detected for device at {device_ip}")
        else:
            print(f"No default password detected for device at {device_ip}")
    except Exception as e:
        print(f"Error checking password for device at {device_ip}: {e}")

# Example usage:
check_default_password("127.0.0.1:5000")

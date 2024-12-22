import requests

# Toggle this variable to switch between environments
USE_PRODUCTION = False

if USE_PRODUCTION:
    BASE_URL = 'https://api.godaddy.com/v1'
    API_KEY = '<Go Daddy API-Key>'
    API_SECRET = '<Go Daddy API-Secret>'
else:
    BASE_URL = 'https://api.ote-godaddy.com/v1'
    API_KEY = '<Go Daddy API-Key>'
    API_SECRET = '<Go Daddy API-Secret>'


def check_domain_godaddy(domain):
    url = f"{BASE_URL}/domains/available?domain={domain}"
    headers = {
        "Authorization": f"sso-key {API_KEY}:{API_SECRET}",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        result = response.json()
        return result["available"]
    elif response.status_code == 403:
        print("Error 403: Access Denied - Check your API key permissions.")
        return None
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None


def main():
    with open('domains.txt', 'r') as file:
        domains = file.readlines()

    with open('available_domains.txt', 'w') as available_domain:
        for word in domains:
            word = word.strip()
            domain = f"{word}.com"
            is_available = check_domain_godaddy(domain)
            if is_available is not None:
                status = "available" if is_available else "taken"
                print(f"The domain {domain} is {status}.")
                if is_available:
                    available_domain.write(domain + " is available" + "\n")


if __name__ == "__main__":
    main()

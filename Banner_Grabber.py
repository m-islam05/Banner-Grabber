import requests

def grab_banner(url):
    # Send a GET request to the URL
    response = requests.get(url)
         
    # Print the banner
    print("\nHTTP Headers (Banner):\n")
    for header, value in response.headers.items():
        print(f"{header}: {value}")
    
    
# Usage
url = "https://example.com"  # Target URL
grab_banner(url)

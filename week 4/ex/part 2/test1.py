import requests

BASE_URL = 'https://fakestoreapi.com'

# response = requests.get(f"{BASE_URL}/products")
# response = requests.get(f"{BASE_URL}/carts")
response = requests.get(f"{BASE_URL}/users")#carts #users #
print(response.json())
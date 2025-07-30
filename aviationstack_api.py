import requests

API_KEY = 'f0a716ca3044d700807af10490cc1c8d'  
BASE_URL = 'http://api.aviationstack.com/v1/'

def get_flights_data(limit=100):
    """
    Fetch real-time flight data (most recent flights) from Aviationstack API.

    Args:
        limit (int): Number of flight records to fetch (default = 100)

    Returns:
        List[Dict]: List of flight data entries (raw JSON format)
    """
    params = {
        'access_key': API_KEY,
        'limit': limit,
        'sort': 'desc'
    }

    try:
        response = requests.get(BASE_URL + 'flights', params=params)
        response.raise_for_status()
        data = response.json()
        return data.get('data', [])
    except Exception as e:
        print(f"Error fetching data: {e}")
        return []

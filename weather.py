import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_current_weather(city="Yerevan"):
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API key is not set in environment variables")

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city}&units=metric'

    try:
        response = requests.get(request_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
    return None
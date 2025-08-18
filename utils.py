import urllib.request

API_URL = "https://wttr.in/{}?format=3"

def get_weather(city):
    try:
        with urllib.request.urlopen(API_URL.format(city)) as response:
            return response.read().decode("utf-8")
    except Exception as e:
        return f"Exception: {e}"

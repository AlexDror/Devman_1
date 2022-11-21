"""
Lesson 1. Weather forecast in console.
"""
import requests
from requests.exceptions import HTTPError


LOCATIONS: tuple = ('London', 'SVO', 'Череповец')
PARAMS: str = 'm3nqT&lang=ru'
URL: str = 'http://wttr.in/'


def print_weather() -> None:
    """
    Prints weather forecast for 3 days in cities, sets in LOCATIONS constant shown above
    """
    for location in LOCATIONS:
        try:
            response: requests.Response = requests.get(URL + location, params=PARAMS, timeout=100)
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        else:
            print(response.text)


if __name__ == '__main__':
    print_weather()

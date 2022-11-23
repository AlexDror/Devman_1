from requests import get, Response
from requests.exceptions import HTTPError, Timeout


LOCATIONS: tuple = ('London', 'SVO', 'Череповец')
PARAMS: dict = {'m3nqT': '', 'lang': 'ru'}
URL: str = 'http://wttr.in'


def print_weather() -> None:
    """
    Prints weather forecast for 3 days in cities, sets in LOCATIONS constant shown above
    """
    for location in LOCATIONS:
        try:
            response: Response = get(f'{URL}/{location}', params=PARAMS, timeout=20)
            response.raise_for_status()

        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Timeout as timeout_error:
            print(f'Website is down temporary... {timeout_error}')
            print('Please try later')
        else:
            print(response.text)


if __name__ == '__main__':
    print_weather()

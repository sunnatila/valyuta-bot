import requests
from pprint import pprint


def valyuta_determiner(sum1: str = "USD", sum2: str = "UZS") -> float:
    url = 'b274bb57510243ea99a70275'
    url1 = f"https://v6.exchangerate-api.com/v6/{url}/pair/{sum1.upper()}/{sum2.upper()}"
    response = requests.get(url1).json()['conversion_rate']
    return response


if __name__ == '__main__':
    pprint(valyuta_determiner())

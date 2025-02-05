from string import punctuation
import requests
from requests import ConnectTimeout
from unidecode import unidecode
from time import sleep

translator = str.maketrans(punctuation, " " * len(punctuation))


def clean_string(string):
    return unidecode(string.lower().translate(translator))


sleep_time = [0]


def check_zip_code(cep):
    while True:
        sleep(sleep_time[0])
        req = requests.get(f"https://cdn.apicep.com/file/apicep/{cep[0:5]}-{cep[5:]}.json").json()
        if req["status"] == 429:
            sleep_time[0] += .5
            try:
                req = requests.get(f"https://viacep.com.br/ws/{cep}/json/").json()
            except ConnectionError or ConnectTimeout:
                continue
            else:
                if "erro" in req:
                    continue
        break
    return req["status"] == 200

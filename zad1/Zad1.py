import requests


class RandomUser:
    def __init__(self):
        self.url = "https://randomuser.me/api"

    def getRandomUser(self):
        r = requests.get(self.url)
        return r.json()['results'][0]

    def get_location(self):
        r = requests.get(self.url)
        return r.json()['results'][0]['location']
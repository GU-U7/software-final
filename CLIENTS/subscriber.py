import requests



class Subscriber:
    def __init__(self):
        self.address = 'http://127.0.0.1:8080/message/'

    def search_topic(self, topic: str) -> str:
        resp = requests.get(self.address+topic)
        return resp.text


pub = Subscriber()
print(pub.search_topic("architecture"))
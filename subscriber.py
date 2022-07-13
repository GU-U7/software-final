import requests


class Publisher:
    def __init__(self):
        self.address = 'http://127.0.0.1:8080'

    def post_message(self, message, topic):
        resp = requests.post(self.address, json={'message':message, 'topic':topic}, headers="application/json")
        print(resp.json())


pub = Publisher()
pub.post_message("HOLAS", "medicine")
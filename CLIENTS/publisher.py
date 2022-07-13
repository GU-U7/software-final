import requests



class Publisher:
    def __init__(self):
        self.address = 'http://127.0.0.1:8080/message'
        self.headers = {"Content-Type": "application/json"}
        self.json = dict()

    def post_message(self, message, topic) -> bool:
        self.json['message'] = message
        self.json['topic'] = topic
        resp = requests.post(self.address, headers=self.headers, json=self.json)
        resp_json = resp.json()
        if resp_json['status'] == 'ok':
            return True
        elif resp_json['status'] == 'fail':
            return False


pub = Publisher()
pub.post_message("HOLAS", "architecture")
import requests

class IssPosition:
    def __init__(self):
        response = requests.get("http://api.open-notify.org/iss-now.json")
        self.latitude = float(response.json()['iss_position']['latitude'])
        self.longitude = float(response.json()['iss_position']['longitude'])


    def get_tracking_state(self):
        while True:
            response = requests.get("http://api.open-notify.org/iss-now.json")
            self.latitude = float(response.json()['iss_position']['latitude'])
            self.longitude = float(response.json()['iss_position']['longitude'])
            return [self.latitude, self.longitude]




import requests


def res_check(res):
    status_code = res.status_code
    if status_code == 200:
        res = res.json()
    else:
        res = {"status_code": status_code}
        print(status_code, res)
    return res


class Communicator:
    def __init__(self, base_url, token="", problem=""):
        self.headers = {'Accept': "application/json",
                        'Content-Type': "application/json"}

        self.base_url = base_url

        self.headers['X-Auth-Token'] = token
        self.headers['Authorization'] = self.post_method("/start", {'problem': problem})["auth_key"]

        print("auth_key:", self.headers["Authorization"])  # if you want to check "/start" and auth_key.

    def get_method(self, sub_url):
        res = requests.get(self.base_url + sub_url, headers=self.headers)
        return res_check(res)

    def post_method(self, sub_url, data):
        res = requests.post(self.base_url + sub_url, headers=self.headers, json=data)
        return res_check(res)

    def put_method(self, sub_url, data):
        res = requests.put(self.base_url + sub_url, headers=self.headers, json=data)
        return res_check(res)


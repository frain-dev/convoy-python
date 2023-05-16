from dataclasses import dataclass
from typing import Optional
import requests
import json
from convoy.utils import response_helper
from base64 import b64encode


@dataclass
class Config:
    api_key: Optional[str] = ""
    uri: Optional[str] = ""
    project_id: Optional[str] = ""

class Client():
    """
    Initializes a Client Object.
    """
    def __init__(self, config: dict):
        config = Config(**config)
        if config.api_key:
            self.api_key = config.api_key

        if config.uri == "":
            self.base_uri = f"https://dashboard.getconvoy.io/api/v1/projects/{config.project_id}"
        else:
            self.base_uri = config.uri

        self.headers = {"Authorization": self.get_authorization(), "Content-Type": "application/json; charset=utf-8"}

    def http_get(self, path, query):
        try:
            response = requests.get(self.build_path(path), headers=self.headers, params=query)
            return response.json(), response.status_code
        except BaseException as e:
            return response_helper(e) 

    def http_post(self, path, query, data):
        try:
            response = requests.post(self.build_path(path), data=json.dumps(data), headers=self.headers, params=query)
            return response.json(), response.status_code
        except BaseException as e:
            return response_helper(e) 

    def http_put(self, path, query, data):
        try:
            response = requests.put(self.build_path(path), data=json.dumps(data), headers=self.headers, params=query)
            return response.json(), response.status_code
        except BaseException as e:
            return response_helper(e) 

    def http_delete(self, path, query, data):
        try:
            response = requests.delete(self.build_path(path), data=json.dumps(data), headers=self.headers, params=query)
            return response.json(), response.status_code
        except BaseException as e:
            return response_helper(e) 

    def get_base_url(self):
        return self.base_uri

    def get_authorization(self):
        try:
            if self.api_key != "":
                return "Bearer %s" % self.api_key
            raise ValueError("Invalid API Key")
        except ValueError as e:
            return e

    def build_path(self, path):
        return "%s%s" % (self.base_uri, path)

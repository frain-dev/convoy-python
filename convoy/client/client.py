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
            self.base_uri = f"{config.uri}/api/v1/projects/{config.project_id}"

        self.headers = {"Authorization": self.get_authorization(), "Content-Type": "application/json; charset=utf-8"}

    def _http_request(self, verb, path, query, data=None):
        try:
            method = getattr(requests, verb)
            response = method(self.build_path(path), headers=self.headers, params=query, data=data)
            return response.json(), response.status_code
        except BaseException as e:
            response_helper(e)

    def http_get(self, path, query):
        return self._http_request('get', path, query)

    def http_post(self, path, query, data):
        return self._http_request('post', path, query, json.dumps(data))

    def http_put(self, path, query, data):
        return self._http_request('put', path, query, json.dumps(data))

    def http_delete(self, path, query, data):
        return self._http_request('delete', path, query, json.dumps(data))

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

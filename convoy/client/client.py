from dataclasses import dataclass
from typing import Optional
import requests
import json
from convoy.utils import response_helper


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

        if not config.api_key:
            raise ValueError("api_key is required")
        if not config.uri:
            raise ValueError("uri is required, e.g. https://us.getconvoy.cloud/api/v1")
        if not config.project_id:
            raise ValueError("project_id is required")
        if "/projects/" in config.uri or config.uri.rstrip("/").endswith("/projects"):
            raise ValueError("uri must be the instance API base without a project path; pass project_id separately")

        self.api_key = config.api_key
        self.base_uri = "%s/projects/%s" % (config.uri.rstrip("/"), config.project_id)
        self.headers = {
            "Authorization": "Bearer %s" % self.api_key,
            "Content-Type": "application/json; charset=utf-8",
            # Pin the API version this SDK release was built against; the
            # server's request migrations translate for older/newer instances.
            "X-Convoy-Version": "2025-11-24",
        }

    def http_get(self, path, query):
        try:
            response = requests.get(self.build_path(path), headers=self.headers, params=query)
            return self.parse_response(response)
        except requests.RequestException as e:
            return response_helper(e)

    def http_post(self, path, query, data):
        try:
            response = requests.post(self.build_path(path), data=json.dumps(data, separators=(",", ":")), headers=self.headers, params=query)
            return self.parse_response(response)
        except requests.RequestException as e:
            return response_helper(e)

    def http_put(self, path, query, data):
        try:
            response = requests.put(self.build_path(path), data=json.dumps(data, separators=(",", ":")), headers=self.headers, params=query)
            return self.parse_response(response)
        except requests.RequestException as e:
            return response_helper(e)

    def http_delete(self, path, query, data):
        try:
            response = requests.delete(self.build_path(path), data=json.dumps(data, separators=(",", ":")), headers=self.headers, params=query)
            return self.parse_response(response)
        except requests.RequestException as e:
            return response_helper(e)

    @staticmethod
    def parse_response(response):
        # Proxies or routers can return non-JSON error bodies; surface them
        # in the standard (body, status_code) shape instead of crashing.
        try:
            return response.json(), response.status_code
        except ValueError:
            return {"status": False, "message": response.text}, response.status_code

    def get_base_url(self):
        return self.base_uri

    def build_path(self, path):
        return "%s%s" % (self.base_uri, path)

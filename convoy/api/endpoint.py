from convoy.client import Client

class Endpoint():
    """Initializes an Endpoint object to make calls to the /endpoints endpoint.
       
    Parameters
    ----------
    config : dict of config values
    """
    def __init__(self, config):
        self.client = Client(config)

    def all(self, query):
        """
        Get all endpoints for a project.
        """
        response = self.client.http_get("/endpoints", query)
        return response

    def create(self, query, data):
        """
        Create a new endpoint.
        Parameters
        ----------
        data = {
                "url": "",
                "description": "",
                "secret": "",
                "events": [],
                }
        """
        response = self.client.http_post("/endpoints", query, data)
        return response

    def find(self, endpoint_id, query):
        """
        Find a particular endpoint.
        """
        response = self.client.http_get("endpoints/%s" % endpoint_id, query)
        return response

    def update(self, endpoint_id, query, data):
        """
        Update an endpoint.
        Parameters
        ---------- 
        data = {
                "url": "",
                "description": "",
                "secret": "",
                "events": [],
                }
        """
        response = self.client.http_put("/endpoints/%s" % endpoint_id, query, data)
        return response

    def delete(self, endpoint_id, query, data):
        """
        Delete an endpoint.
        """
        response = self.client.http_delete("/endpoints/%s" % endpoint_id, query, data)
        return response


from convoy.client import Client

class Endpoint():
    """Initializes an Endpoint object to make calls to the /endpoints endpoint.
       
    Parameters
    ----------
    config : dict of config values
    """
    def __init__(self, config):
        self.client = Client(config)

    def all(self, app_id, query):
        """
        Get all endpoints for an application.
        """
        response = self.client.http_get("/applications/%s/endpoints" % app_id, query)
        return response

    def create(self, app_id, query, data):
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
        response = self.client.http_post("/applications/%s/endpoints" % app_id, query, data)
        return response

    def find(self, app_id, endpoint_id, query):
        """
        Find a particular application.
        """
        response = self.client.http_get("/applications/%s/endpoints/%s" % (app_id, endpoint_id), query)
        return response

    def update(self, app_id, endpoint_id, query, data):
        """
        Update an application.
        Parameters
        ---------- 
        data = {
                "url": "",
                "description": "",
                "secret": "",
                "events": [],
                }
        """
        response = self.client.http_put("/applications/%s/endpoints/%s" % (app_id, endpoint_id), query, data)
        return response

    def delete(self, app_id, endpoint_id, query, data):
        """
        Delete an application.
        """
        response = self.client.http_delete("/applications/%s/endpoints/%s" % (app_id, endpoint_id), query, data)
        return response


from convoy.client import Client

class Project():
    """Initializes a Project object scoped to the configured project.

    Parameters
    ----------
    config : dict of config values
    """
    def __init__(self, config):
        self.client = Client(config)

    def find(self, query):
        """
        Retrieve the configured project.
        """
        response = self.client.http_get("", query)
        return response

    def update(self, query, data):
        """
        Update the configured project.
        Parameters
        ----------
        data = {
            "name": "",
            "logo_url": "",
            "config": {},
        }
        """
        response = self.client.http_put("", query, data)
        return response

    def delete(self, query):
        """
        Delete the configured project.
        """
        response = self.client.http_delete("", query, {})
        return response

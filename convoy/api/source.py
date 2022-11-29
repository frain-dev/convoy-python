from convoy.client import Client

class Source():
    """Initializes a Source object to make calls to the source endpoint.

    Parameters
    ----------
    config: dict of config values       
    """

    def __init__(self, config):
        self.client = Client(config)

    def all(self, query):
        """
        Get all sources for a project.
        """

        response = self.client.http_get("/sources", query)
        return response

    def create(self, query, data):
        """
        Create a new source.

        Paramters
        ---------
        data = {
            {
            "name": "",
            "type": "",
                "provider": "",
                "verifier": {
                    "hmac": {
                        "secret": ""
                    }
                }
        }
        """

        response = self.client.http_post("/sources", query, data)
        return response

    def find(self, source_id, query):
        """
        Find a source by supplied ID.
        """

        response = self.client.http_get("/sources/%s" % source_id, query)
        return response

    def update(self, source_id, query, data):
        """
        Update a source.

        Parameters
        ----------
        data = {
            "is_disabled": true | false,
            "name": "",
            "provider": "",
            "type": "",
            "verifier": {
                "api_key": {
                "header_name": "",
                "header_value": ""
                },
                "basic_auth": {
                "password": "",
                "username": ""
                },
                "hmac": {
                "encoding": "",
                "hash": "",
                "header": "",
                "secret": ""
                },
                "type": ""
            }
            }
        """
    
        response = self.client.http_put("/sources/%s" % source_id, query, data)
        return response

    def delete(self, source_id, query, data):
        """
        Delete a source.
        """

        response = self.client.http_delete("/sources/%s" % source_id, query, data)
        return response
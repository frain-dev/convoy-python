from convoy.client import Client

class Event():
    """Initializes an Event object to make calls to the /event endpoint.
       
    Parameters
    ----------
    config : dict of config values
    """
    def __init__(self, config):
        self.client = Client(config)

    def all(self, query):
        response = self.client.http_get("/events", query)
        return response

    def create(self, query, data):
        """
        Create a new event.
        Parameters
        ----------
        data = {
                endpoint_id: "",
                event_type: "",
                data: {
                        "event": "",
                        "data": {},
                    }
                }
        """
        response = self.client.http_post("/events", query, data)
        return response

    def find(self, id, query):
        response = self.client.http_get("/events/%s" % id, query)
        return response


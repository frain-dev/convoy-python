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

    def fanout(self, query, data):
        """
        Send an event to all endpoints with the given owner_id.
        Parameters
        ----------
        data = {
                "owner_id": "",
                "event_type": "",
                "data": {},
                }
        """
        response = self.client.http_post("/events/fanout", query, data)
        return response

    def broadcast(self, query, data):
        """
        Send an event to all endpoints in the project.
        Parameters
        ----------
        data = {
                "event_type": "",
                "data": {},
                }
        """
        response = self.client.http_post("/events/broadcast", query, data)
        return response

    def replay(self, id):
        """
        Replay a previously ingested event.
        """
        response = self.client.http_put("/events/%s/replay" % id, {}, {})
        return response


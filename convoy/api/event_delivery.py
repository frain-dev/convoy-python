from convoy.client import Client

class EventDelivery():
    """Initializes an EventDelivery object to make calls to the /eventdeliveries endpoint.
       
    Parameters
    ----------
    config : dict of config values
    """
    def __init__(self, config):
        self.client = Client(config)

    def all(self, query):
        """
        Get all eventdeliveries.
        """
        response = self.client.http_get("/eventdeliveries", query)
        return response

    def find(self, id, query):
        """
        Find a particular eventdelivery.    
        """
        response = self.client.http_get("/eventdeliveries/%s" % id, query)
        return response

    def resend(self, id, query):
        """
        Resend an eventdelivery.    
        """
        response = self.client.http_put("/eventdeliveries/%s/resend" % id, query, {})
        return response

    def batchresend(self, query):
        """
        Batch retry eventdeliveries matching the query filters. The server
        reads filters from query params only, e.g.
        query = {"endpointId": [], "eventId": "", "status": []}
        """
        response = self.client.http_post("/eventdeliveries/batchretry", query, {})
        return response

    def forceresend(self, query, data):
        """
        Force resend successful eventdeliveries.
        Parameters
        ----------
        data = {
                "ids": []
                }
        """
        response = self.client.http_post("/eventdeliveries/forceresend", query, data)
        return response


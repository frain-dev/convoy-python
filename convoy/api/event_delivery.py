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

    def batchresend(self, id, query, data):
        """
        Batch resend eventdeliveries.
        Parameters
        ----------
        data = {
                ids: []
                }
        """
        response = self.client.http_put("/eventdeliveries/batchretry" % id, query, data)
        return response


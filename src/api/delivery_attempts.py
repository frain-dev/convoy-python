from client import Client

class DeliveryAttempt():
    """Initializes a DeliveryAttempt object to make calls to the /deliveryattempts endpoint.
       
    Parameters
    ----------
    config : dict of config values
    """
    def __init__(self, config):
        self.client = Client(config)

    def all(self, eventdeliveryId, query):
        response = self.client.httpGet("/eventdeliveries/%s/deliveryattempts" %  eventdeliveryId, query)
        return response

    def find(self, eventdeliveryId, deliveryAttemptId, query):
        response = self.client.httpGet("/eventdeliveries/%s/deliveryattempts/%s" %  (eventdeliveryId, deliveryAttemptId), query)
        return response


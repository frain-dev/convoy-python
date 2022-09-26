from convoy.client import Client

class DeliveryAttempt():
    """Initializes a DeliveryAttempt object to make calls to the /delivery_attempts endpoint.
       
    Parameters
    ----------
    config : dict of config values
    """
    def __init__(self, config):
        self.client = Client(config)

    def all(self, event_delivery_id, query):
        response = self.client.http_get("/eventdeliveries/%s/deliveryattempts" %  event_delivery_id, query)
        return response

    def find(self, event_delivery_id, delivery_attempt_id, query):
        response = self.client.http_get("/eventdeliveries/%s/deliveryattempts/%s" %  (event_delivery_id, delivery_attempt_id), query)
        return response


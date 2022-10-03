from re import sub
from convoy.api import application, delivery_attempts, endpoint, event, event_delivery, group, source, subscription

class Convoy():
    """Initializes the main Convoy Object.
       
    Parameters
    ----------
    config : dict of config values, see example config below;

    config = {
        #Username used for basic authentication
        "username": "",
        #Password used for basic authentication
        "password": "",
        #API Key used for bearer token authentication
        "api_key": "",
        #Convoy self hosted uri
        "uri": ""
    }
    """
    def __init__(self, config):
        self.applications = application.Application(config)
        self.delivery_attempts = delivery_attempts.DeliveryAttempt(config)
        self.endpoint = endpoint.Endpoint(config)
        self.event_delivery = event_delivery.EventDelivery(config)
        self.event = event.Event(config)
        self.group = group.Group(config)
        self.source = source.Source(config)
        self.subscription = subscription.Subscription(config)
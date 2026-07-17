"""Speakeasy migration: hand-written HTTP API is deprecated; next major replaces this with OpenAPI-generated clients. Webhook verify stays hand-written."""
from convoy.api import delivery_attempts, endpoint, event, event_delivery, project, source, subscription
from convoy.utils import webhook

class Convoy():
    """Initializes the main Convoy Object.
       
    Parameters
    ----------
    config : dict of config values, see example config below;

    config = {
        #API Key used for bearer token authentication
        "api_key": "",
        #Convoy instance API base, e.g. https://us.getconvoy.cloud/api/v1
        "uri": "",
        #Project ID from your project settings page
        "project_id": ""
    }
    """
    def __init__(self, config):
        self.delivery_attempt = delivery_attempts.DeliveryAttempt(config)
        self.endpoint = endpoint.Endpoint(config)
        self.event_delivery = event_delivery.EventDelivery(config)
        self.event = event.Event(config)
        self.project = project.Project(config)
        self.source = source.Source(config)
        self.subscription = subscription.Subscription(config)
        self.webhook = webhook.Webhook()

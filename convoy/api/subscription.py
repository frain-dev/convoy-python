from convoy.client import Client

class Subscription():
    """Initializes a Subscription object to make calls to the subscription endpoint.

    Parameters
    ----------
    config: dict of config values
    
    """

    def __init__(self, config):
        self.client = Client(config)

    def all(self, query):
        """
        Get all subscriptions.
        """

        response = self.client.http_get("/subscriptions", query)
        return response

    def create(self, query, data):
        """
        Create a new subscription.

        Parameters
        ----------
        data = {
            "alert_config": {
                "count": 0,
                "threshold": ""
            },
            "app_id": "",
            "endpoint_id": "",
            "filter_config": {
                "event_types": []
            },
            "name": "string",
            "retry_config": {
                "duration": "",
                "retry_count": 0,
                "type": ""
            },
            "source_id": ""
            }
        """

        response = self.client.http_post("/subscriptions", query, data)
        return response

    def find(self, subscription_id, query):
        """
        Find a subscription by supplied ID.
        """

        response = self.client.http_get("/subscriptions/%s" % subscription_id, query)
        return response

    def update(self, subscription_id, query, data):
        """
        Update a subscription.

        Parameters
        ----------
        data = {
            "alert_config": {
                "count": 0,
                "threshold": ""
            },
            "app_id": "",
            "endpoint_id": "",
            "filter_config": {
                "event_types": []
            },
            "name": "string",
            "retry_config": {
                "duration": "",
                "retry_count": 0,
                "type": ""
            },
            "source_id": ""
            }
        """

        response = self.client.http_put("/subscriptions/%s" % subscription_id, query, data)
        return response

    def delete(self, subscription_id, query, data):
        """
        Delete a subscription.
        """

        response = self.client.http_delete("/subscriptions/%s" % subscription_id, query, data)
        return response

from client import Client

class Endpoint():
    """Initializes an Endpoint object to make calls to the /endpoints endpoint.
       
    Parameters
    ----------
    config : dict of config values
    """
    def __init__(self, config):
        self.client = Client(config)

    def all(self, appId, query):
        '''
        Get all endpoints for an application.
        '''
        response = self.client.httpGet("/applications/%s/endpoints" % appId, query)
        return response

    def create(self, appId, query, data):
        '''
        Create a new endpoint.
        Parameters
        ----------
        data = {
                "url": "",
                "description": "",
                "secret": "",
                "events": [],
                }
        '''
        response = self.client.httpPost("/applications/%s/endpoints" % appId, query, data)
        return response

    def find(self, appId, endpointId, query):
        '''
        Find a particular application.
        '''
        response = self.client.httpGet("/applications/%s/endpoints/%s" % (appId, endpointId), query)
        return response

    def update(self, appId, endpointId, query, data):
        '''
        Update an application.
        Parameters
        ---------- 
        data = {
                "url": "",
                "description": "",
                "secret": "",
                "events": [],
                }
        '''
        response = self.client.httpPut("/applications/%s/endpoints/%s" % (appId, endpointId), query, data)
        return response

    def delete(self, appId, endpointId, query, data):
        '''
        Delete an application.
        '''
        response = self.client.httpDelete("/applications/%s/endpoints/%s" % (appId, endpointId), query, data)
        return response


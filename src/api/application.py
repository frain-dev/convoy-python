from client import Client

class Application():
    """Initializes an Application object to make calls to the /application endpoint.
       
    Parameters
    ----------
    config : dict of config values
    """
    def __init__(self, config):
        self.client = Client(config)

    def all(self, query):
        '''
        Get all applicaitons.
        '''
        response = self.client.httpGet("/applications", query)
        return response

    def create(self, query, data):
        '''
        Create a new application.
        Parameters
        ----------
        data = {
                "name": "",
                "support_email": "",
                "secret": ""
                }
        '''
        response = self.client.httpPost("/applications", query, data)
        return response

    def find(self, id, query):
        '''
        Find a particular application.    
        '''
        response = self.client.httpGet("/applications/%s" % (id), query)
        return response

    def update(self, id, query, data):
        '''
        Update an application.
        Parameters
        ---------- 
        data = {
                "name": "",
                "support_email": "",
                "secret": ""
                }
        '''
        response = self.client.httpPut("/applications/%s" % id, query, data)
        return response

    def delete(self, id, query, data):
        '''
        Delete an application.
        '''
        response = self.client.httpDelete("/applications/%s" % id, query, data)
        return response


from client import Client

class Group():
    """Initializes a Groups object to make calls to the /groups endpoint.
       
    Parameters
    ----------
    config : dict of config values
    """
    def __init__(self, config):
        self.client = Client(config)

    def all(self, query):
        '''
        Get all groups.
        '''
        response = self.client.httpGet("/groups", query)
        return response

    def create(self, query, data):
        '''
        Create a new group.
        Parameters
        ----------
        data = {
            "name": "",
            "logo_url": "",
            "config": {
                    "disable_endpoint": bool,
                    "signature": {
                                "hash": "",
                                "header": ""
                                },
                    "strategy": {
                                "type":   "",
                                "default": {
                                    "intervalSeconds": int,
                                    "retryLimit": int
                            }
                        },
                    },
                }
        '''
        response = self.client.httpPost("/groups", query, data)
        return response

    def find(self, id, query):
        '''
        Find a particular group.    
        '''
        response = self.client.httpGet("/groups/%s" % id, query)
        return response

    def update(self, id, query, data):
        '''
        Update a group.
        Parameters
        ---------- 
        data = {
            "name": "",
            "logo_url": "",
            "config": {
                    "disable_endpoint": bool,
                    "signature": {
                                "hash": "",
                                "header": ""
                                },
                    "strategy": {
                                "type":   "",
                                "default": {
                                    "intervalSeconds": int,
                                    "retryLimit": int
                            }
                        },
                    },
                }
        '''
        response = self.client.httpPut("/groups/%s" % id, query, data)
        return response

    def delete(self, id, query, data):
        '''
        Delete a group.
        '''
        response = self.client.httpDelete("/groups/%s" % id, query, data)
        return response


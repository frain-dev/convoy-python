"""
You can use these dict objects to create your own data.
"""

Config = {
        #Username used for basic authentication
        "username": "",
        #Password used for basic authentication
        "password": "",
        #API Key used for bearer token authentication
        "api_key": "",
        #Convoy self hosted uri
        "uri": ""
    }

NewEvent = {
            "endpoint_id": "",
            "event_type": "",
            "data": {
                    "event": "",
                    "data": {},
                }
            }

NewEndpoint = {
                "url": "",
                "description": "",
                "secret": "",
                "events": [],
                }

BatchResend = {
                "ids": []
            }


NewGroup = {
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




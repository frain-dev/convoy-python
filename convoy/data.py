"""
You can use these dict objects to create your own data.
"""

Config = {
        #API Key used for bearer token authentication
        "api_key": "",
        #Convoy instance API base, e.g. https://us.getconvoy.cloud/api/v1
        "uri": "",
        #Project ID from your project settings page
        "project_id": ""
    }

NewEvent = {
            "endpoint_id": "",
            "event_type": "",
            "data": {},
            }

NewFanoutEvent = {
            "owner_id": "",
            "event_type": "",
            "data": {},
            }

NewBroadcastEvent = {
            "event_type": "",
            "data": {},
            }

NewEndpoint = {
                "name": "",
                "url": "",
                "description": "",
                "secret": "",
                "content_type": "",
                }

NewSubscription = {
                "name": "",
                "endpoint_id": "",
                }

# Body for event_delivery.forceresend; batchresend takes query filters only.
ForceResend = {
                "ids": []
            }

UpdateProject = {
            "name": "",
            "logo_url": "",
            "config": {},
            }

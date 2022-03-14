from convoy import Convoy
from convoy.data import *
from convoy.client import Client

Config["api_key"] = "your-api-key"

cnv = Convoy(Config)

#Application
def test_application():
    NewApplication["name"] = "pythonsdktestapp"
    NewApplication["support_email"] = "testsdk@frain.dev"
    _, status = cnv.applications.create({"groupID":"449f4d86-e70b-40eb-a733-dadd89d8d3b6"}, NewApplication)
    assert(status == 201)
    # response = cnv.applications.all("groupID=449f4d86-e70b-40eb-a733-dadd89d8d3b6")
    # response = cnv.applications.find("fb05c3c7-2d9c-4e07-95b4-e859c1415385", "groupID=449f4d86-e70b-40eb-a733-dadd89d8d3b6")
    # UpdateApplication = NewApplication
    # UpdateApplication["name"] = "sdktest_app"
    # response = cnv.applications.update("9a3cc2b9-ce09-4dbd-9ea9-594def3dd347", "groupID=449f4d86-e70b-40eb-a733-dadd89d8d3b6", UpdateApplication)

#Endpoint
def test_endpoint():
    NewEndpoint["url"] = "http://ed0b-102-219-153-85.ngrok.io"
    NewEndpoint["description"] = "testendpoint"
    _, status = cnv.endpoint.create("9a3cc2b9-ce09-4dbd-9ea9-594def3dd347", {"groupID":"449f4d86-e70b-40eb-a733-dadd89d8d3b6"}, NewEndpoint)
    assert(status == 201)
    # response = cnv.endpoint.all("fb05c3c7-2d9c-4e07-95b4-e859c1415385", {"groupID":"449f4d86-e70b-40eb-a733-dadd89d8d3b6"})
    # response = cnv.endpoint.find("fb05c3c7-2d9c-4e07-95b4-e859c1415385", {"groupID":"449f4d86-e70b-40eb-a733-dadd89d8d3b6"}, "7ebfde76-ad24-4913-b516-72a8a8e14735")
    # UpdateEndpoint = NewEndpoint
    # UpdateEndpoint["description"] = "test_endpoint"
    # response = cnv.endpoint.update("a535e91a-2fd2-40e4-95d5-138df62a63db","5523df4f-0bf0-4d6a-9c36-064306b8b7d2", {"groupID":"449f4d86-e70b-40eb-a733-dadd89d8d3b6"}, UpdateEndpoint)
    # response = cnv.endpoint.delete("a535e91a-2fd2-40e4-95d5-138df62a63db","5523df4f-0bf0-4d6a-9c36-064306b8b7d2", {"groupID":"449f4d86-e70b-40eb-a733-dadd89d8d3b6"}, "")

#EventDelivery
def test_eventdelivery():    
    content, status = cnv.eventDelivery.all({"groupID":"449f4d86-e70b-40eb-a733-dadd89d8d3b6"})
    assert(len(content) > 0)
    assert(status == 200)
    # response = cnv.eventDelivery.find("dfa306bd-ef49-4528-8175-a363e01c4623", {})

#Event
def test_event():
    NewEvent["app_id"] = "9a3cc2b9-ce09-4dbd-9ea9-594def3dd347"
    NewEvent["event_type"] = "payment.success"
    NewEvent["data"] = {
                        "event": "payment.success",
                        "data": {
                            "status": "Completed",
                            "description": "Transaction Successful",
                            "userID": "test_user_id808",
                            "paymentReference": "test_ref_85149",
                            "amount": 200,
                            "senderAccountName": "Alan Christian Segun",
                            "sourceAccountNumber": "2999993564",
                            "sourceAccountType": "personal",
                            "sourceBankCode": "50211",
                            "destinationAccountNumber": "00855584818",
                            "destinationBankCode": "063"
                        },
                    }
    content, status = cnv.event.create({"groupID":"449f4d86-e70b-40eb-a733-dadd89d8d3b6"}, NewEvent)
    assert(len(content) > 0)
    assert(status == 201)
    # response = cnv.event.all({"groupID":"449f4d86-e70b-40eb-a733-dadd89d8d3b6"})
    # response = cnv.event.find("89b0574d-24fd-44a8-b902-bb679b543506", {"groupID":"449f4d86-e70b-40eb-a733-dadd89d8d3b6"})

# #Group
def test_group():
    NewGroup = {
                "name": "pythonsdk",
                "logo_url": "",
                "config": {
                        "disable_endpoint": False,
                        "signature": {
                                    "hash": "SHA256",
                                    "header": "X_PYTHONSDK_APP"
                                    },
                        "strategy": {
                                    "type": "default",
                                    "default": {
                                        "intervalSeconds": 5,
                                        "retryLimit": 3
                                }
                            },
                        },
                    }

    # content, status = cnv.group.create({"groupID":"449f4d86-e70b-40eb-a733-dadd89d8d3b6"}, NewGroup)
    content, status = cnv.group.all({"groupID":"449f4d86-e70b-40eb-a733-dadd89d8d3b6"})
    assert(status == 200)
    # response = cnv.group.find("96d04e60-854c-4f7e-9257-be88c15474fd", {"groupID":"449f4d86-e70b-40eb-a733-dadd89d8d3b6"})
    # UpdateGroup = NewGroup
    # UpdateGroup["name"] = "convoypythonsdk"
    # response  = cnv.group.update("f46f780a-4216-4306-b1ba-1c5e0a30086e", {"groupID":"449f4d86-e70b-40eb-a733-dadd89d8d3b6"}, UpdateGroup)

#DeliveryAttempts
def test_deliverattempts():
    content, status = cnv.deliveryAttempts.all("6bb26fe3-a3d8-4ea8-aa7c-55bd61caa8be", {"groupID":"449f4d86-e70b-40eb-a733-dadd89d8d3b6"})
    assert(status == 404)
    # response  = cnv.deliveryAttempts.find("dfa306bd-ef49-4528-8175-a363e01c4623", "1d1e3b81-3a33-472b-9380-a8c8afa06252", {})

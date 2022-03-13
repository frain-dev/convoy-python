import requests

def responseHelper(e):
    if e == requests.exceptions.HTTPError:
        print ("Http Error:", e)
    if e == requests.exceptions.ConnectionError:
        print ("Error Connecting:", e)
    if e == requests.exceptions.Timeout:
        print ("Timeout Error:", e)
    if e == requests.exceptions.RequestException:
        print(e)
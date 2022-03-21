from logging import exception
import requests
import hmac
import hashlib
import base64

def responseHelper(e):
    if e == requests.exceptions.HTTPError:
        raise Exception("Http Error: %s" % e)
    if e == requests.exceptions.ConnectionError:
        raise Exception("Error Connecting: %s" % e)
    if e == requests.exceptions.Timeout:
        raise Exception("Timeout Error: %s" % e)
    if e == requests.exceptions.RequestException:
        raise Exception(e)
    else:
        raise Exception(e)

def verifySignature(algorithm, hmac, payload, secret):
    '''
    algorithm: hash algorithm e.g SHA256
    hmac: the signed payload 
    payload: the unsigned payload
    secret: secret that was used for hashing
    '''
    dec = hashString(algorithm, payload, secret)
    return dec == hash

def hashString(algorithm, msg, secret):
    alg = getHashFunction(str.lower(algorithm)) 
    dig = hmac.new(bytes(secret, 'utf-8'), msg=bytes(msg, 'utf-8'), digestmod=alg).digest()
    dec = base64.b64encode(dig).decode()
    return dec

def getHashFunction(hash):
    if str.lower(hash) == 'sha256':
        return hashlib.sha256
    if str.lower(hash) == 'md5':
        return hashlib.md5
    if str.lower(hash) == 'sha384':
        return hashlib.sha384
    if str.lower(hash) == 'sha224':
        return hashlib.sha224
    if str.lower(hash) == 'sha512':
        return hashlib.sha512
    if str.lower(hash) == 'sha1':
        return hashlib.sha1
    if str.lower(hash) == 'sha3_256':
        return hashlib.sha3_256
    if str.lower(hash) == 'sha3_224':
        return hashlib.sha3_224 
    if str.lower(hash) == 'sha3_512':
        return hashlib.sha3_512 
    else:
        raise Exception("algorithm not available.")
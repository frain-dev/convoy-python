import pytest

from convoy.utils.webhook import Webhook

# Vectors generated with the server's signature scheme (pkg/signature):
# simple = HMAC(secret, payload), advanced = HMAC(secret, "{t},{payload}").
# The advanced timestamp is far in the future so tolerance never expires.
SIMPLE_PAYLOAD = '{"mode":"sig-simple","n":42}'
SIMPLE_SECRET = "sig-simple-secret"
SIMPLE_HEX = "eaa91c1f2dfc842e8873a895d75dfd2d5757c622f0b6d6022d6d48864d41d2fc"
SIMPLE_B64 = "6qkcHy38hC6Ic6iV1139LVdXxiLwttYCLW1Ihk1B0vw="

ADV_PAYLOAD = '{"mode":"sig-adv","n":42}'
ADV_SECRET = "sig-adv-secret"
ADV_HEX_HEADER = "t=2048976161,v1=a89599858951cff83b61ca2f50b8138af92e09388be7723c28a380397c1a8391"
ADV_B64_HEADER = "t=2048976161,v1=qJWZhYlRz/g7YcovULgTivkuCTiL53I8KKOAOXwag5E="


def test_verify_simple_hex_signature():
    webhook = Webhook(secret=SIMPLE_SECRET)
    assert webhook.verify_signature(SIMPLE_PAYLOAD, SIMPLE_HEX) is True


def test_verify_simple_base64_signature():
    webhook = Webhook(secret=SIMPLE_SECRET, encoding="base64")
    assert webhook.verify_signature(SIMPLE_PAYLOAD, SIMPLE_B64) is True


def test_verify_simple_dict_payload():
    webhook = Webhook(secret=SIMPLE_SECRET)
    assert webhook.verify_signature({"mode": "sig-simple", "n": 42}, SIMPLE_HEX) is True


def test_reject_tampered_simple_payload():
    webhook = Webhook(secret=SIMPLE_SECRET)
    assert webhook.verify_signature(SIMPLE_PAYLOAD.replace("42", "43"), SIMPLE_HEX) is not True


def test_reject_wrong_simple_secret():
    webhook = Webhook(secret="wrong-secret")
    assert webhook.verify_signature(SIMPLE_PAYLOAD, SIMPLE_HEX) is not True


def test_verify_advanced_hex_signature():
    webhook = Webhook(secret=ADV_SECRET)
    assert webhook.verify_signature(ADV_PAYLOAD, ADV_HEX_HEADER) is True


def test_verify_advanced_base64_signature():
    webhook = Webhook(secret=ADV_SECRET, encoding="base64")
    assert webhook.verify_signature(ADV_PAYLOAD, ADV_B64_HEADER) is True


def test_reject_tampered_advanced_payload():
    webhook = Webhook(secret=ADV_SECRET)
    assert webhook.verify_signature(ADV_PAYLOAD.replace("42", "43"), ADV_HEX_HEADER) is not True


def test_reject_expired_advanced_timestamp():
    webhook = Webhook(secret=ADV_SECRET)
    expired = "t=1000000000,v1=" + ADV_HEX_HEADER.split("v1=")[1]
    assert webhook.verify_signature(ADV_PAYLOAD, expired) is not True


def test_reject_expired_timestamp_even_with_valid_signature():
    # Fail-closed: a signature correctly computed for an old timestamp
    # must still be rejected once the timestamp exceeds tolerance.
    import hashlib
    import hmac as hmac_mod

    old_t = 1000000000
    signed = f"{old_t},{ADV_PAYLOAD}"
    sig = hmac_mod.new(ADV_SECRET.encode(), signed.encode(), hashlib.sha256).hexdigest()
    webhook = Webhook(secret=ADV_SECRET)
    assert webhook.verify_signature(ADV_PAYLOAD, f"t={old_t},v1={sig}") is not True


def test_multi_signature_header_accepts_any_valid():
    valid_sig = ADV_HEX_HEADER.split("v1=")[1]
    header = "t=2048976161,v1=" + "0" * 64 + ",v1=" + valid_sig
    webhook = Webhook(secret=ADV_SECRET)
    assert webhook.verify_signature(ADV_PAYLOAD, header) is True


def test_advanced_header_timestamp_not_first():
    valid_sig = ADV_HEX_HEADER.split("v1=")[1]
    header = "v1=" + valid_sig + ",t=2048976161"
    webhook = Webhook(secret=ADV_SECRET)
    assert webhook.verify_signature(ADV_PAYLOAD, header) is True

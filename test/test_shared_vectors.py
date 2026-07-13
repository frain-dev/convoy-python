import json
import os

import pytest

from convoy.utils.webhook import Webhook

# signature-vectors.json is generated from the server signing code
# (convoy/pkg/signature) and vendored here so this SDK verifies against the same
# canonical set as every other Convoy SDK. Regenerate upstream with
# CONVOY_WRITE_VECTORS=1 go test ./pkg/signature -run TestGenerateSignatureVectors
VECTORS_PATH = os.path.join(os.path.dirname(__file__), "signature-vectors.json")

with open(VECTORS_PATH) as f:
    VECTORS = json.load(f)


@pytest.mark.parametrize("vec", VECTORS, ids=[v["name"] for v in VECTORS])
def test_shared_signature_vector(vec):
    webhook = Webhook(
        secret=vec["secret"],
        encoding=vec["encoding"],
        tolerance=vec["tolerance"],
        hash=vec["hash"],
    )

    result = webhook.verify_signature(vec["payload"], vec["header"])

    # Strict identity checks: an invalid vector must return exactly False, never a
    # truthy value (e.g. an error string), which would make `if verify(...)` pass
    # a forged webhook.
    if vec["valid"]:
        assert result is True, vec["name"]
    else:
        assert result is False, vec["name"]

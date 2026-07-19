from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_endpoint_authentication import ModelsEndpointAuthentication
    from ..models.models_mtls_client_cert import ModelsMtlsClientCert


T = TypeVar("T", bound="ModelsCreateEndpoint")


@_attrs_define
class ModelsCreateEndpoint:
    """
    Attributes:
        advanced_signatures (bool | Unset): Convoy supports two [signature formats](https://getconvoy.io/docs/product-
            manual/signatures)
            -- simple or advanced. If left unspecified, we default to false.
        app_id (str | Unset): Deprecated but necessary for backward compatibility
        authentication (ModelsEndpointAuthentication | Unset):
        content_type (str | Unset): Content type for the endpoint. Defaults to application/json if not specified.
        description (str | Unset): Human-readable description of the endpoint. Think of this as metadata describing
            the endpoint
        http_timeout (int | Unset): Define endpoint http timeout in seconds.
        is_disabled (bool | Unset): This is used to manually enable/disable the endpoint.
        mtls_client_cert (ModelsMtlsClientCert | Unset):
        name (str | Unset): Endpoint name.
        owner_id (str | Unset): The OwnerID is used to group more than one endpoint together to achieve
            [fanout](https://getconvoy.io/docs/manual/endpoints#Endpoint%20Owner%20ID)
        rate_limit (int | Unset): Rate limit is the total number of requests to be sent to an endpoint in
            the time duration specified in RateLimitDuration
        rate_limit_duration (int | Unset): Rate limit duration specifies the time range for the rate limit.
        secret (str | Unset): Endpoint's webhook secret. If not provided, Convoy autogenerates one for the endpoint.
        slack_webhook_url (str | Unset): Slack webhook URL is an alternative method to support email where endpoint
            developers
            can receive failure notifications on a slack channel.
        support_email (str | Unset): Endpoint developers support email. This is used for communicating endpoint state
            changes. You should always turn this on when disabling endpoints are enabled.
        url (str | Unset): URL is the endpoint's URL prefixed with https. non-https urls are currently
            not supported.
    """

    advanced_signatures: bool | Unset = UNSET
    app_id: str | Unset = UNSET
    authentication: ModelsEndpointAuthentication | Unset = UNSET
    content_type: str | Unset = UNSET
    description: str | Unset = UNSET
    http_timeout: int | Unset = UNSET
    is_disabled: bool | Unset = UNSET
    mtls_client_cert: ModelsMtlsClientCert | Unset = UNSET
    name: str | Unset = UNSET
    owner_id: str | Unset = UNSET
    rate_limit: int | Unset = UNSET
    rate_limit_duration: int | Unset = UNSET
    secret: str | Unset = UNSET
    slack_webhook_url: str | Unset = UNSET
    support_email: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        advanced_signatures = self.advanced_signatures

        app_id = self.app_id

        authentication: dict[str, Any] | Unset = UNSET
        if not isinstance(self.authentication, Unset):
            authentication = self.authentication.to_dict()

        content_type = self.content_type

        description = self.description

        http_timeout = self.http_timeout

        is_disabled = self.is_disabled

        mtls_client_cert: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mtls_client_cert, Unset):
            mtls_client_cert = self.mtls_client_cert.to_dict()

        name = self.name

        owner_id = self.owner_id

        rate_limit = self.rate_limit

        rate_limit_duration = self.rate_limit_duration

        secret = self.secret

        slack_webhook_url = self.slack_webhook_url

        support_email = self.support_email

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if advanced_signatures is not UNSET:
            field_dict["advanced_signatures"] = advanced_signatures
        if app_id is not UNSET:
            field_dict["appID"] = app_id
        if authentication is not UNSET:
            field_dict["authentication"] = authentication
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if description is not UNSET:
            field_dict["description"] = description
        if http_timeout is not UNSET:
            field_dict["http_timeout"] = http_timeout
        if is_disabled is not UNSET:
            field_dict["is_disabled"] = is_disabled
        if mtls_client_cert is not UNSET:
            field_dict["mtls_client_cert"] = mtls_client_cert
        if name is not UNSET:
            field_dict["name"] = name
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if rate_limit is not UNSET:
            field_dict["rate_limit"] = rate_limit
        if rate_limit_duration is not UNSET:
            field_dict["rate_limit_duration"] = rate_limit_duration
        if secret is not UNSET:
            field_dict["secret"] = secret
        if slack_webhook_url is not UNSET:
            field_dict["slack_webhook_url"] = slack_webhook_url
        if support_email is not UNSET:
            field_dict["support_email"] = support_email
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_endpoint_authentication import ModelsEndpointAuthentication
        from ..models.models_mtls_client_cert import ModelsMtlsClientCert

        d = dict(src_dict)
        advanced_signatures = d.pop("advanced_signatures", UNSET)

        app_id = d.pop("appID", UNSET)

        _authentication = d.pop("authentication", UNSET)
        authentication: ModelsEndpointAuthentication | Unset
        if isinstance(_authentication, Unset):
            authentication = UNSET
        else:
            authentication = ModelsEndpointAuthentication.from_dict(_authentication)

        content_type = d.pop("content_type", UNSET)

        description = d.pop("description", UNSET)

        http_timeout = d.pop("http_timeout", UNSET)

        is_disabled = d.pop("is_disabled", UNSET)

        _mtls_client_cert = d.pop("mtls_client_cert", UNSET)
        mtls_client_cert: ModelsMtlsClientCert | Unset
        if isinstance(_mtls_client_cert, Unset):
            mtls_client_cert = UNSET
        else:
            mtls_client_cert = ModelsMtlsClientCert.from_dict(_mtls_client_cert)

        name = d.pop("name", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        rate_limit = d.pop("rate_limit", UNSET)

        rate_limit_duration = d.pop("rate_limit_duration", UNSET)

        secret = d.pop("secret", UNSET)

        slack_webhook_url = d.pop("slack_webhook_url", UNSET)

        support_email = d.pop("support_email", UNSET)

        url = d.pop("url", UNSET)

        models_create_endpoint = cls(
            advanced_signatures=advanced_signatures,
            app_id=app_id,
            authentication=authentication,
            content_type=content_type,
            description=description,
            http_timeout=http_timeout,
            is_disabled=is_disabled,
            mtls_client_cert=mtls_client_cert,
            name=name,
            owner_id=owner_id,
            rate_limit=rate_limit,
            rate_limit_duration=rate_limit_duration,
            secret=secret,
            slack_webhook_url=slack_webhook_url,
            support_email=support_email,
            url=url,
        )

        models_create_endpoint.additional_properties = d
        return models_create_endpoint

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatastoreOAuth2SigningKey")


@_attrs_define
class DatastoreOAuth2SigningKey:
    """
    Attributes:
        crv (str | Unset): EC (Elliptic Curve) key fields
        d (str | Unset): Private key (EC only)
        dp (str | Unset): RSA first factor CRT exponent (RSA private key only)
        dq (str | Unset): RSA second factor CRT exponent (RSA private key only)
        e (str | Unset): RSA public exponent (RSA only)
        kid (str | Unset): Key ID
        kty (str | Unset): Key type: "EC" or "RSA"
        n (str | Unset): RSA key fields
        p (str | Unset): RSA first prime factor (RSA private key only)
        q (str | Unset): RSA second prime factor (RSA private key only)
        qi (str | Unset): RSA first CRT coefficient (RSA private key only)
        x (str | Unset): X coordinate (EC only)
        y (str | Unset): Y coordinate (EC only)
    """

    crv: str | Unset = UNSET
    d: str | Unset = UNSET
    dp: str | Unset = UNSET
    dq: str | Unset = UNSET
    e: str | Unset = UNSET
    kid: str | Unset = UNSET
    kty: str | Unset = UNSET
    n: str | Unset = UNSET
    p: str | Unset = UNSET
    q: str | Unset = UNSET
    qi: str | Unset = UNSET
    x: str | Unset = UNSET
    y: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        crv = self.crv

        d = self.d

        dp = self.dp

        dq = self.dq

        e = self.e

        kid = self.kid

        kty = self.kty

        n = self.n

        p = self.p

        q = self.q

        qi = self.qi

        x = self.x

        y = self.y

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if crv is not UNSET:
            field_dict["crv"] = crv
        if d is not UNSET:
            field_dict["d"] = d
        if dp is not UNSET:
            field_dict["dp"] = dp
        if dq is not UNSET:
            field_dict["dq"] = dq
        if e is not UNSET:
            field_dict["e"] = e
        if kid is not UNSET:
            field_dict["kid"] = kid
        if kty is not UNSET:
            field_dict["kty"] = kty
        if n is not UNSET:
            field_dict["n"] = n
        if p is not UNSET:
            field_dict["p"] = p
        if q is not UNSET:
            field_dict["q"] = q
        if qi is not UNSET:
            field_dict["qi"] = qi
        if x is not UNSET:
            field_dict["x"] = x
        if y is not UNSET:
            field_dict["y"] = y

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        crv = d.pop("crv", UNSET)

        d = d.pop("d", UNSET)

        dp = d.pop("dp", UNSET)

        dq = d.pop("dq", UNSET)

        e = d.pop("e", UNSET)

        kid = d.pop("kid", UNSET)

        kty = d.pop("kty", UNSET)

        n = d.pop("n", UNSET)

        p = d.pop("p", UNSET)

        q = d.pop("q", UNSET)

        qi = d.pop("qi", UNSET)

        x = d.pop("x", UNSET)

        y = d.pop("y", UNSET)

        datastore_o_auth_2_signing_key = cls(
            crv=crv,
            d=d,
            dp=dp,
            dq=dq,
            e=e,
            kid=kid,
            kty=kty,
            n=n,
            p=p,
            q=q,
            qi=qi,
            x=x,
            y=y,
        )

        datastore_o_auth_2_signing_key.additional_properties = d
        return datastore_o_auth_2_signing_key

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

"""
Factory for creating boto3 clients and resources.

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Generic, TypeVar

from botocore.client import BaseClient
from typing_extensions import Unpack

from boto34.boto3.type_defs import ClientKwargs, ResourceKwargs
from boto34.exceptions import Boto34Error

try:
    from boto3.resources.base import ServiceResource
except ImportError as e:
    raise Boto34Error("boto3 is not installed. Install `boto34[boto3]`") from e

if TYPE_CHECKING:
    from boto34.boto3.session import Session

_Client = TypeVar("_Client", bound=BaseClient)
_ServiceResource = TypeVar("_ServiceResource", bound=ServiceResource)


class ServiceFactory(Generic[_Client]):
    SERVICE_NAME: str = ""
    _SERVICE_PROP: str = "service"

    def __init__(self, session: Session) -> None:
        self._session = session

    def client(
        self,
        service_name: str | None = None,
        **kwargs: Unpack[ClientKwargs],
    ) -> _Client:
        result: _Client = self._session.client(
            service_name=self.SERVICE_NAME,
            **kwargs,
        )
        return result

    def get_available_regions(
        self,
        service_name: str | None = None,
        partition_name: str = "aws",
        allow_non_regional: bool = False,
    ) -> list[str]:
        return self._session.get_available_regions(
            service_name=self.SERVICE_NAME,
            partition_name=partition_name,
            allow_non_regional=allow_non_regional,
        )


class ServiceResourceFactory(
    ServiceFactory[_Client],
    Generic[_Client, _ServiceResource],
):
    def resource(
        self,
        service_name: str | None = None,
        **kwargs: Unpack[ResourceKwargs],
    ) -> _ServiceResource:
        result: _ServiceResource = self._session.resource(
            service_name=self.SERVICE_NAME,
            **kwargs,
        )
        return result

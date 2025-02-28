"""
Service session wrapper for aioboto3.

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from collections.abc import Awaitable
from typing import TYPE_CHECKING, Generic, TypeVar

from typing_extensions import Unpack

from boto34.aioboto3.type_defs import ClientKwargs, ResourceKwargs
from boto34.exceptions import Boto34Error

try:
    from aioboto3.resources.base import AIOBoto3ServiceResource
    from aioboto3.session import ResourceCreatorContext
    from aiobotocore.client import AioBaseClient
    from aiobotocore.session import ClientCreatorContext
except ImportError as e:
    raise Boto34Error("aioboto3 is not installed. Install `boto34[aioboto3]`") from e

if TYPE_CHECKING:
    from boto34.aioboto3.session import Session

_Client = TypeVar("_Client", bound=AioBaseClient)
_ServiceResource = TypeVar("_ServiceResource", bound=AIOBoto3ServiceResource)


class ServiceFactory(Generic[_Client]):
    """
    Service session wrapper for aioboto3.

    Attributes:
        service_name: botocore service name
        session: Underlying aioboto3.Session
    """

    def __init__(self, service_name: str, session: Session) -> None:
        self.service_name = service_name
        self.session = session

    def client(
        self,
        service_name: str | None = None,
        **kwargs: Unpack[ClientKwargs],
    ) -> ClientCreatorContext[_Client]:
        """
        Proxy method to aioboto3.session.Session.client.

        Arguments are the same, but service_name is ignored.
        """
        return self.session.client(service_name=self.service_name, **kwargs)

    def get_available_regions(
        self,
        service_name: str | None = None,
        partition_name: str = "aws",
        allow_non_regional: bool = False,
    ) -> Awaitable[list[str]]:
        """
        Proxy method to aioboto3.session.Session.get_available_regions.

        Arguments are the same, but service_name is ignored.
        """
        result: Awaitable[list[str]]
        result = self.session.get_available_regions(  # type: ignore[assignment]
            service_name=self.service_name,
            partition_name=partition_name,
            allow_non_regional=allow_non_regional,
        )
        return result


class ServiceResourceFactory(
    ServiceFactory[_Client],
    Generic[_Client, _ServiceResource],
):
    def resource(
        self,
        service_name: str | None = None,
        **kwargs: Unpack[ResourceKwargs],
    ) -> ResourceCreatorContext[_ServiceResource]:
        """
        Proxy method to aioboto3.session.Session.resource.

        Arguments are the same, but service_name is ignored.
        """
        return self.session.resource(service_name=self.service_name, **kwargs)

"""
Service session wrapper for aiobotocore.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Generic, TypeVar, Unpack

from aioboto3.session import ResourceCreatorContext
from aiobotocore.session import ClientCreatorContext

from boto34.boto3.type_defs import ClientKwargs, ResourceKwargs
from boto34.kwargs_cache import KwargsCache

if TYPE_CHECKING:
    from boto34.aioboto3.session import Session

_Client = TypeVar("_Client")
_ServiceResource = TypeVar("_ServiceResource")


class ServiceFactory(Generic[_Client, _ServiceResource]):
    """
    Service session wrapper for aiobotocore.
    """

    SERVICE_NAME: str = ""
    _SERVICE_PROP: str = "service"

    def __init__(self, session: Session) -> None:
        self._session = session
        self._client_cache = KwargsCache[ClientCreatorContext[_Client]]()
        self._resource_cache = KwargsCache[ResourceCreatorContext[_ServiceResource]]()

    def _client(self, **kwargs: Unpack[ClientKwargs]) -> ClientCreatorContext[_Client]:
        filtered_kwargs = {k: v for k, v in kwargs.items() if v is not None}
        cached_client = self._client_cache.get(filtered_kwargs)
        if cached_client:
            return cached_client
        client = self._session.client(
            service_name=self.SERVICE_NAME,
            **filtered_kwargs,
        )
        self._client_cache.set(filtered_kwargs, client)
        return client

    def _resource(
        self, **kwargs: Unpack[ResourceKwargs]
    ) -> ResourceCreatorContext[_ServiceResource]:
        filtered_kwargs = {k: v for k, v in kwargs.items() if v is not None}
        cached_resource = self._resource_cache.get(filtered_kwargs)
        if cached_resource:
            return cached_resource
        resource = self._session.resource(
            service_name=self.SERVICE_NAME,
            **filtered_kwargs,
        )
        self._resource_cache.set(filtered_kwargs, resource)
        return resource

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

    def clear_cache(self) -> None:
        """
        Clear the client cache.
        """
        self._client_cache.clear()

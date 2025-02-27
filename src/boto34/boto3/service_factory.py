from __future__ import annotations

from typing import TYPE_CHECKING, Generic, TypeVar, Unpack

from boto34.boto3.paginator_factory import PaginatorFactory
from boto34.boto3.type_defs import ClientKwargs, ResourceKwargs
from boto34.boto3.waiter_factory import WaiterFactory
from boto34.exceptions import Boto34Error
from boto34.kwargs_cache import KwargsCache

if TYPE_CHECKING:
    from boto34.boto3.session import Session

_Client = TypeVar("_Client")
_ServiceResource = TypeVar("_ServiceResource")
_WaiterFactory = TypeVar("_WaiterFactory", bound=WaiterFactory | None)
_PaginatorFactory = TypeVar("_PaginatorFactory", bound=PaginatorFactory | None)


class ServiceFactory(
    Generic[_Client, _ServiceResource, _WaiterFactory, _PaginatorFactory]
):
    SERVICE_NAME: str = ""
    _SERVICE_PROP: str = "service"
    _WAITER_FACTORY_CLS: type[_WaiterFactory] | None = None
    _PAGINATOR_FACTORY_CLS: type[_PaginatorFactory] | None = None

    def __init__(self, session: Session) -> None:
        self._session = session
        self._client_cache = KwargsCache[_Client]()
        self._resource_cache = KwargsCache[_ServiceResource]()

    def _client(self, **kwargs: Unpack[ClientKwargs]) -> _Client:
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

    def _resource(self, **kwargs: Unpack[ResourceKwargs]) -> _ServiceResource:
        filtered_kwargs = {k: v for k, v in kwargs.items() if v is not None}
        cached_resource = self._client_cache.get(filtered_kwargs)
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

    def _get_waiter_factory(self) -> _WaiterFactory:
        if not self._WAITER_FACTORY_CLS:
            raise Boto34Error(f"Service {self.SERVICE_NAME} does not have waiters.")

        client = self._client_cache.get_first()
        if client is None:
            raise Boto34Error(
                f"Client not initialized, create it with session.{self._SERVICE_PROP}.client()"
            )

        return self._WAITER_FACTORY_CLS(client)

    def _get_paginator_factory(self) -> _PaginatorFactory:
        if not self._WAITER_FACTORY_CLS:
            raise Boto34Error(f"Service {self.SERVICE_NAME} does not have paginators.")

        client = self._client_cache.get_first()
        if client is None:
            raise Boto34Error(
                f"Client not initialized, create it with session.{self._SERVICE_PROP}.client()"
            )

        return self._PAGINATOR_FACTORY_CLS(client)

    def clear_cache(self) -> None:
        self._client_cache.clear()
        self._resource_cache.clear()

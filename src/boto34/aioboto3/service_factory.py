"""
Service session wrapper for aiobotocore.

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Generic, TypeVar

from aioboto3.resources.base import AIOBoto3ServiceResource
from aioboto3.session import ResourceCreatorContext
from aiobotocore.client import AioBaseClient
from aiobotocore.session import ClientCreatorContext
from typing_extensions import Unpack

from boto34.aioboto3.client_factory import ClientFactory
from boto34.aioboto3.type_defs import ClientKwargs, ResourceKwargs
from boto34.exceptions import Boto34Error

if TYPE_CHECKING:
    from boto34.aioboto3.session import Session

_Client = TypeVar("_Client", bound=AioBaseClient)
_ServiceResource = TypeVar("_ServiceResource", bound=AIOBoto3ServiceResource)
_WaiterFactory = TypeVar("_WaiterFactory", bound=ClientFactory[Any])
_PaginatorFactory = TypeVar("_PaginatorFactory", bound=ClientFactory[Any])


class ServiceFactory(Generic[_Client, _WaiterFactory, _PaginatorFactory]):
    """
    Service session wrapper for aiobotocore.
    """

    SERVICE_NAME: str = ""
    _SERVICE_PROP: str = "service"
    _WAITER_FACTORY_CLS: type[_WaiterFactory] | None = None
    _PAGINATOR_FACTORY_CLS: type[_PaginatorFactory] | None = None

    def __init__(self, session: Session) -> None:
        self._session = session

    def client(
        self,
        service_name: str | None = None,
        **kwargs: Unpack[ClientKwargs],
    ) -> ClientCreatorContext[_Client]:
        """
        Proxy method to aioboto3.session.Session.client.

        Arguments are the same, but service_name is ignored.
        """
        return self._session.client(service_name=self.SERVICE_NAME, **kwargs)

    def get_available_regions(
        self,
        service_name: str | None = None,
        partition_name: str = "aws",
        allow_non_regional: bool = False,
    ) -> list[str]:
        """
        Proxy method to aioboto3.session.Session.get_available_regions.

        Arguments are the same, but service_name is ignored.
        """
        return self._session.get_available_regions(
            service_name=self.SERVICE_NAME,
            partition_name=partition_name,
            allow_non_regional=allow_non_regional,
        )

    def _get_waiter_factory(self, client: _Client) -> _WaiterFactory:
        if not self._WAITER_FACTORY_CLS:
            raise Boto34Error(f"Service {self.SERVICE_NAME} does not have waiters.")

        return self._WAITER_FACTORY_CLS(client)

    def _get_paginator_factory(self, client: _Client) -> _PaginatorFactory:
        if not self._PAGINATOR_FACTORY_CLS:
            raise Boto34Error(f"Service {self.SERVICE_NAME} does not have paginators.")

        return self._PAGINATOR_FACTORY_CLS(client)


class ServiceResourceFactory(
    ServiceFactory[_Client, _WaiterFactory, _PaginatorFactory],
    Generic[_Client, _ServiceResource, _WaiterFactory, _PaginatorFactory],
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
        return self._session.resource(service_name=self.SERVICE_NAME, **kwargs)

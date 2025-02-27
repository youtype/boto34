"""
Service session wrapper for aiobotocore.

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Generic, TypeVar

from aiobotocore.client import AioBaseClient
from aiobotocore.session import ClientCreatorContext
from botocore.model import ServiceModel
from typing_extensions import Unpack

from boto34.aiobotocore.client_factory import ClientFactory
from boto34.aiobotocore.type_defs import ClientKwargs
from boto34.exceptions import Boto34Error

if TYPE_CHECKING:
    from boto34.aiobotocore.session import Session

_Client = TypeVar("_Client", bound=AioBaseClient)
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

    def create_client(
        self,
        service_name: str | None = None,
        **kwargs: Unpack[ClientKwargs],
    ) -> ClientCreatorContext[_Client]:
        """
        Proxy method to aiobotocore.session.Session.create_client.

        Arguments are the same, but service_name is ignored.
        """
        return self._session.create_client(service_name=self.SERVICE_NAME, **kwargs)

    async def get_service_model(
        self, service_name: str | None = None, api_version: str | None = None
    ) -> ServiceModel:
        """
        Proxy method to aiobotocore.session.Session.get_service_model.

        Arguments are the same, but service_name is ignored.
        """
        return await self._session.get_service_model(self.SERVICE_NAME, api_version)

    async def get_service_data(
        self, service_name: str | None = None, api_version: str | None = None
    ) -> dict[str, Any]:
        """
        Proxy method to aiobotocore.session.Session.get_service_data.

        Arguments are the same, but service_name is ignored.
        """
        return await self._session.get_service_data(self.SERVICE_NAME, api_version)

    async def get_available_regions(
        self,
        service_name: str | None = None,
        partition_name: str = "aws",
        allow_non_regional: bool = False,
    ) -> list[str]:
        """
        Proxy method to aiobotocore.session.Session.get_available_regions.

        Arguments are the same, but service_name is ignored.
        """
        return await self._session.get_available_regions(
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

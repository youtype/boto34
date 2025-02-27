"""
Service session wrapper for aiobotocore.
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

    def _create_client(
        self, **kwargs: Unpack[ClientKwargs]
    ) -> ClientCreatorContext[_Client]:
        filtered_kwargs: ClientKwargs = {}
        for key, value in kwargs.items():
            if value is not None:
                filtered_kwargs[key] = value
        return self._session.create_client(
            service_name=self.SERVICE_NAME,
            **filtered_kwargs,
        )

    async def get_service_model(  # type: ignore[override]
        self, service_name: str | None = None, api_version: Any | None = None
    ) -> ServiceModel:
        return await self._session.get_service_model(self.SERVICE_NAME, api_version)

    async def get_service_data(
        self, service_name: str | None = None, api_version: Any | None = None
    ) -> dict[str, Any]:
        return await self._session.get_service_data(self.SERVICE_NAME, api_version)

    async def get_available_regions(
        self,
        service_name: str | None = None,
        partition_name: str = "aws",
        allow_non_regional: bool = False,
    ) -> list[str]:
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
